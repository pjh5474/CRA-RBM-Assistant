interface EssentialDocumentsHeaderProps {
	siteName: string;
}

export function EssentialDocumentsHeader({
	siteName,
}: EssentialDocumentsHeaderProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<p className="mb-2 text-sm font-semibold text-blue-700">
				Essential Document Readiness Tracker
			</p>

			<h1 className="text-2xl font-bold text-slate-900">{siteName}</h1>

			<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
				This page summarizes site-level essential document readiness using
				structured document status data. It is designed to demonstrate how
				document completeness, missing items, pending items, and expired
				documents can be tracked for CRA monitoring preparation.
			</p>
		</section>
	);
}
