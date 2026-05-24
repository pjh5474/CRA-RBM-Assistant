"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { createSupabaseBrowserClient } from "@/lib/supabase/client";
import type { User } from "@supabase/supabase-js";

export default function AuthStatus() {
	const supabase = createSupabaseBrowserClient();
	const [user, setUser] = useState<User | null>(null);
	const [isLoading, setIsLoading] = useState(true);

	useEffect(() => {
		async function loadUser() {
			const {
				data: { user },
			} = await supabase.auth.getUser();

			setUser(user);
			setIsLoading(false);
		}

		loadUser();

		const {
			data: { subscription },
		} = supabase.auth.onAuthStateChange((_event, session) => {
			setUser(session?.user ?? null);
		});

		return () => {
			subscription.unsubscribe();
		};
	}, [supabase.auth]);

	async function handleSignOut() {
		await supabase.auth.signOut();
		setUser(null);
		window.location.reload();
	}

	if (isLoading) {
		return <span className="text-sm text-slate-500">Checking auth...</span>;
	}

	if (!user) {
		return (
			<Link
				href="/login"
				className="rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-800"
			>
				Sign in
			</Link>
		);
	}

	return (
		<div className="flex flex-wrap items-center gap-3">
			<span className="text-sm text-slate-600">
				Signed in as{" "}
				<span className="font-medium text-slate-900">{user.email}</span>
			</span>

			<button
				type="button"
				onClick={handleSignOut}
				className="rounded-xl border border-slate-300 bg-white px-4 py-2 text-sm font-semibold text-slate-700 hover:bg-slate-50"
			>
				Sign out
			</button>
		</div>
	);
}
