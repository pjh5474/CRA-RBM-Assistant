import Link from "next/link";

export function StudyImportHeader() {
	return (
		<>
			<div>
				<Link href="/" className="text-sm font-medium text-blue-700">
					← Back to study list
				</Link>
			</div>

			<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
				<p className="mb-2 text-sm font-semibold text-blue-700">
					ClinicalTrials.gov Study Search
				</p>
				<h1 className="text-2xl font-bold text-slate-900">
					Import Public Study Preview
				</h1>
				<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
					Search public clinical trial registry data and preview structured
					study information. This page currently supports search and preview
					only. Importing selected studies into Supabase can be added in the
					next step.
				</p>
			</section>
		</>
	);
}
