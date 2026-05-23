import { MonitoringReportFinding } from "@/types/monitoringReport";

interface FindingCardProps {
	finding: MonitoringReportFinding;
	index: number;
}

export function FindingCard({ finding, index }: FindingCardProps) {
	return (
		<article className="rounded-xl border border-slate-200 bg-slate-50 p-5">
			<div className="mb-3 flex flex-wrap items-center gap-2">
				<span className="rounded-full bg-slate-900 px-3 py-1 text-xs font-semibold text-white">
					Finding {index}
				</span>
				<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
					{finding.category}
				</span>
			</div>

			<div className="space-y-4">
				<div>
					<p className="mb-1 text-xs font-semibold uppercase tracking-wide text-slate-500">
						Finding
					</p>
					<p className="text-sm leading-6 text-slate-800">{finding.finding}</p>
				</div>

				<div>
					<p className="mb-1 text-xs font-semibold uppercase tracking-wide text-slate-500">
						Recommended CRA Follow-up
					</p>
					<p className="text-sm leading-6 text-slate-800">
						{finding.recommendedAction}
					</p>
				</div>
			</div>
		</article>
	);
}
