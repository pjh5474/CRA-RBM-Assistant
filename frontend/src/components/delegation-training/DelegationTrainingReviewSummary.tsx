import { DelegationTrainingCheck } from "@/types/delegationTraining";

interface DelegationTrainingReviewSummaryProps {
	check: DelegationTrainingCheck;
}

export function DelegationTrainingReviewSummary({
	check,
}: DelegationTrainingReviewSummaryProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="text-lg font-bold text-slate-900">CRA Review Summary</h2>

			{check.issueRecords === 0 ? (
				<p className="mt-3 text-sm leading-6 text-slate-700">
					All delegation and training records are currently consistent with the
					delegation start date. CRA should continue routine delegation log and
					training evidence review.
				</p>
			) : (
				<div className="mt-3 space-y-2 text-sm leading-6 text-slate-700">
					<p>
						This site has {check.issueRecords} delegation/training issue(s)
						requiring CRA review.
					</p>

					<ul className="space-y-1">
						{check.missingTrainingRecords > 0 && (
							<li>
								- {check.missingTrainingRecords} record(s) have missing GCP or
								protocol training evidence.
							</li>
						)}

						{check.trainingAfterDelegationRecords > 0 && (
							<li>
								- {check.trainingAfterDelegationRecords} record(s) show training
								completed after delegation start date.
							</li>
						)}

						<li>
							- CRA should reconcile delegation log, training evidence, and
							delegated task timing.
						</li>
					</ul>
				</div>
			)}
		</section>
	);
}
