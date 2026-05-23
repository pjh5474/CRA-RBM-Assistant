import { SiteReviewSummary } from "@/types/siteReview";

interface SiteReviewCraSummaryProps {
	review: SiteReviewSummary;
}

export function SiteReviewCraSummary({ review }: SiteReviewCraSummaryProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="text-lg font-bold text-slate-900">CRA Review Summary</h2>

			<p className="mt-3 text-sm leading-7 text-slate-700">
				{review.monitoringReportDraft.summary}
			</p>

			{review.site.riskFactors.length > 0 && (
				<div className="mt-4">
					<p className="mb-2 text-sm font-semibold text-slate-900">
						Key Risk Factors
					</p>
					<div className="flex flex-wrap gap-2">
						{review.site.riskFactors.map((factor) => (
							<span
								key={factor}
								className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700"
							>
								{factor}
							</span>
						))}
					</div>
				</div>
			)}
		</section>
	);
}
