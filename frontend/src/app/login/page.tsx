"use client";

import Link from "next/link";
import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import { createSupabaseBrowserClient } from "@/lib/supabase/client";

export default function LoginPage() {
	const router = useRouter();
	const supabase = createSupabaseBrowserClient();

	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	const [isSigningIn, setIsSigningIn] = useState(false);
	const [isSigningUp, setIsSigningUp] = useState(false);
	const [message, setMessage] = useState<string | null>(null);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);

	async function handleSignIn(event: FormEvent<HTMLFormElement>) {
		event.preventDefault();

		try {
			setIsSigningIn(true);
			setErrorMessage(null);
			setMessage(null);

			const { error } = await supabase.auth.signInWithPassword({
				email,
				password,
			});

			if (error) {
				setErrorMessage(error.message);
				return;
			}

			setMessage("Signed in successfully.");
			router.push("/");
			router.refresh();
		} finally {
			setIsSigningIn(false);
		}
	}

	async function handleSignUp() {
		try {
			setIsSigningUp(true);
			setErrorMessage(null);
			setMessage(null);

			const { error } = await supabase.auth.signUp({
				email,
				password,
			});

			if (error) {
				setErrorMessage(error.message);
				return;
			}

			setMessage(
				"Sign-up request completed. Please check your email if confirmation is required.",
			);
		} finally {
			setIsSigningUp(false);
		}
	}

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-md space-y-6">
				<Link href="/" className="text-sm font-medium text-blue-700">
					← Back to study list
				</Link>

				<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
					<p className="mb-2 text-sm font-semibold text-blue-700">
						CRA-RBM Assistant
					</p>

					<h1 className="text-2xl font-bold text-slate-900">Sign in</h1>

					<p className="mt-3 text-sm leading-6 text-slate-600">
						Sign in to use write operations such as importing public studies
						from ClinicalTrials.gov. Public dashboards remain available without
						sign-in.
					</p>

					<form onSubmit={handleSignIn} className="mt-6 space-y-4">
						<div>
							<label className="mb-1 block text-sm font-medium text-slate-700">
								Email
							</label>
							<input
								type="email"
								value={email}
								onChange={(event) => setEmail(event.target.value)}
								required
								className="w-full rounded-xl border border-slate-300 px-4 py-2.5 text-sm outline-none focus:border-blue-600 focus:ring-2 focus:ring-blue-100"
							/>
						</div>

						<div>
							<label className="mb-1 block text-sm font-medium text-slate-700">
								Password
							</label>
							<input
								type="password"
								value={password}
								onChange={(event) => setPassword(event.target.value)}
								required
								className="w-full rounded-xl border border-slate-300 px-4 py-2.5 text-sm outline-none focus:border-blue-600 focus:ring-2 focus:ring-blue-100"
							/>
						</div>

						{errorMessage && (
							<p className="rounded-xl bg-red-50 px-4 py-3 text-sm text-red-700">
								{errorMessage}
							</p>
						)}

						{message && (
							<p className="rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-700">
								{message}
							</p>
						)}

						<div className="flex flex-col gap-3 sm:flex-row">
							<button
								type="submit"
								disabled={isSigningIn}
								className="rounded-xl bg-blue-700 px-4 py-2.5 text-sm font-semibold text-white hover:bg-blue-800 disabled:cursor-not-allowed disabled:bg-slate-400"
							>
								{isSigningIn ? "Signing in..." : "Sign in"}
							</button>

							<button
								type="button"
								onClick={handleSignUp}
								disabled={isSigningUp || !email || !password}
								className="rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm font-semibold text-slate-700 hover:bg-slate-50 disabled:cursor-not-allowed disabled:bg-slate-100 disabled:text-slate-400"
							>
								{isSigningUp ? "Signing up..." : "Sign up"}
							</button>
						</div>
					</form>
				</section>
			</div>
		</main>
	);
}
