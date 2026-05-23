import { getDocumentIssueCount } from "@/lib/essentialDocument";
import { EssentialDocumentReadiness } from "@/types/essentialDocument";

interface DocumentStatusSummaryProps {
	readiness: EssentialDocumentReadiness;
}

export function DocumentStatusSummary({
	readiness,
}: DocumentStatusSummaryProps) {
	const issueCount = getDocumentIssueCount(readiness);

	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="text-lg font-bold text-slate-900">CRA Review Summary</h2>

			{issueCount === 0 ? (
				<p className="mt-3 text-sm leading-6 text-slate-700">
					All required essential documents are currently marked as ready for
					this site. CRA should continue routine document reconciliation during
					monitoring.
				</p>
			) : (
				<div className="mt-3 space-y-2 text-sm leading-6 text-slate-700">
					<p>
						This site has {issueCount} document readiness issue(s) requiring CRA
						follow-up.
					</p>

					<ul className="space-y-1">
						{readiness.missingDocuments > 0 && (
							<li>
								- {readiness.missingDocuments} missing document(s) require site
								file reconciliation.
							</li>
						)}
						{readiness.pendingDocuments > 0 && (
							<li>
								- {readiness.pendingDocuments} pending document(s) require
								confirmation.
							</li>
						)}
						{readiness.expiredDocuments > 0 && (
							<li>
								- {readiness.expiredDocuments} expired document(s) require
								updated evidence or retraining documentation.
							</li>
						)}
					</ul>
				</div>
			)}
		</section>
	);
}
