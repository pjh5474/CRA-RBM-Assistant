"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { getAccessibleStudies } from "@/lib/api";
import { createSupabaseBrowserClient } from "@/lib/supabase/client";
import { StudySummary } from "@/types/study";
import AuthStatus from "@/components/auth/AuthStatus";

export default function StudyListClient() {
	const supabase = createSupabaseBrowserClient();

	const [studies, setStudies] = useState<StudySummary[]>([]);
	const [isLoading, setIsLoading] = useState(true);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);

	async function loadStudies() {
		try {
			setIsLoading(true);
			setErrorMessage(null);

			const {
				data: { session },
			} = await supabase.auth.getSession();

			const accessToken = session?.access_token;

			const data = await getAccessibleStudies(accessToken);

			setStudies(data);
		} catch (error) {
			console.error(error);
			setErrorMessage("Failed to load accessible studies.");
		} finally {
			setIsLoading(false);
		}
	}

	useEffect(() => {
		loadStudies();

		const {
			data: { subscription },
		} = supabase.auth.onAuthStateChange(() => {
			loadStudies();
		});

		return () => {
			subscription.unsubscribe();
		};
	}, []);

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<div className="flex flex-wrap items-center justify-between gap-4">
					<div>
						<p className="mb-2 text-sm font-semibold text-blue-700">
							CRA-RBM Assistant
						</p>

						<h1 className="text-3xl font-bold text-slate-900">
							Accessible Studies
						</h1>

						<p className="mt-3 max-w-3xl text-sm leading-6 text-slate-600">
							Public demo studies are available without sign-in. Imported
							studies owned by your account are shown after sign-in.
						</p>
					</div>

					<AuthStatus />
				</div>

				<div className="flex flex-wrap gap-3">
					<Link
						href="/study-import"
						className="rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-800"
					>
						Import ClinicalTrials.gov Study
					</Link>

					<Link
						href="/audit-logs"
						className="rounded-xl border border-slate-300 bg-white px-4 py-2 text-sm font-semibold text-slate-700 hover:bg-slate-50"
					>
						View Audit Logs
					</Link>
				</div>

				{isLoading && (
					<section className="rounded-2xl border border-slate-200 bg-white p-8 text-sm text-slate-600 shadow-sm">
						Loading accessible studies...
					</section>
				)}

				{errorMessage && (
					<section className="rounded-2xl border border-red-200 bg-red-50 p-5 text-sm text-red-700">
						{errorMessage}
					</section>
				)}

				{!isLoading && !errorMessage && studies.length === 0 && (
					<section className="rounded-2xl border border-dashed border-slate-300 bg-white p-10 text-center">
						<h2 className="text-lg font-semibold text-slate-900">
							No accessible studies
						</h2>
						<p className="mt-2 text-sm text-slate-600">
							No public demo studies or owned imported studies were found. Sign
							in and import a ClinicalTrials.gov study to create one.
						</p>
					</section>
				)}

				{!isLoading && !errorMessage && studies.length > 0 && (
					<section className="grid gap-4 md:grid-cols-2">
						{studies.map((study) => (
							<Link
								key={study.studyId}
								href={`/studies/${study.studyId}`}
								className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-md"
							>
								<div className="mb-3 flex flex-wrap gap-2">
									<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
										{study.phase}
									</span>
									<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
										{study.studyId}
									</span>
								</div>

								<h2 className="text-lg font-bold text-slate-900">
									{study.title}
								</h2>

								<p className="mt-3 text-sm leading-6 text-slate-600">
									{study.indication}
								</p>

								<p className="mt-4 text-sm font-medium text-slate-700">
									Sponsor: {study.sponsor}
								</p>
							</Link>
						))}
					</section>
				)}
			</div>
		</main>
	);
}
