import { ProtocolDeviationSummary } from "@/types/protocolDeviation";

interface DeviationReviewSummaryProps {
	summary: ProtocolDeviationSummary;
}

export function DeviationReviewSummary({
	summary,
}: DeviationReviewSummaryProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="text-lg font-bold text-slate-900">CRA Review Summary</h2>

			{summary.totalDeviations === 0 ? (
				<p className="mt-3 text-sm leading-6 text-slate-700">
					No protocol deviations were identified for this site. CRA should
					continue routine protocol compliance monitoring.
				</p>
			) : (
				<div className="mt-3 space-y-2 text-sm leading-6 text-slate-700">
					<p>
						This site has {summary.totalDeviations} protocol deviation
						record(s), including {summary.openDeviations} open item(s).
					</p>

					<ul className="space-y-1">
						{summary.criticalDeviations > 0 && (
							<li>
								- {summary.criticalDeviations} critical deviation(s) require
								immediate CRA review and escalation consideration.
							</li>
						)}
						{summary.majorDeviations > 0 && (
							<li>
								- {summary.majorDeviations} major deviation(s) require root
								cause review and corrective/preventive action follow-up.
							</li>
						)}
						{summary.openDeviations > 0 && (
							<li>
								- Open deviation(s) should be tracked until resolution and
								documentation completion.
							</li>
						)}
					</ul>
				</div>
			)}
		</section>
	);
}
