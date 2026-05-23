import { SummaryCard } from "@/components/ui/SummaryCard";
import { getTotalFollowUpSignals } from "@/lib/siteReview";
import { SiteReviewSummary } from "@/types/siteReview";

interface SiteReviewSummaryGridProps {
	review: SiteReviewSummary;
}

export function SiteReviewSummaryGrid({ review }: SiteReviewSummaryGridProps) {
	const issueCount = getTotalFollowUpSignals(review);

	return (
		<section className="grid gap-4 md:grid-cols-5">
			<SummaryCard
				title="Risk Factors"
				value={review.site.riskFactors.length}
			/>
			<SummaryCard
				title="Document Readiness"
				value={`${review.essentialDocuments.readinessScore}%`}
			/>
			<SummaryCard
				title="Open Deviations"
				value={review.protocolDeviations.openDeviations}
			/>
			<SummaryCard
				title="ICF Issues"
				value={review.icfVersionCheck.issueConsents}
			/>
			<SummaryCard title="Total Follow-up Signals" value={issueCount} />
		</section>
	);
}
