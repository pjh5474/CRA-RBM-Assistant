import { ClinicalTrialDetail } from "@/types/clinicalTrial";

interface PreviewGridProps {
	study: ClinicalTrialDetail;
}

export function PreviewGrid({ study }: PreviewGridProps) {
	const rows = [
		{ label: "Study Type", value: study.studyType },
		{ label: "Allocation", value: study.allocation },
		{ label: "Masking", value: study.masking },
		{ label: "Who Masked", value: study.whoMasked.join(", ") },
		{ label: "Phase", value: study.phases.join(", ") },
		{ label: "Conditions", value: study.conditions.join(", ") },
		{ label: "Interventions", value: study.interventions.join(", ") },
	];

	return (
		<div className="grid gap-3 md:grid-cols-2">
			{rows.map((row) => (
				<div
					key={row.label}
					className="rounded-xl border border-slate-200 bg-slate-50 p-4"
				>
					<p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
						{row.label}
					</p>
					<p className="mt-2 text-sm text-slate-900">
						{row.value || "Not available"}
					</p>
				</div>
			))}
		</div>
	);
}
