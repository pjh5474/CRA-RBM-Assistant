import { SiteReviewSummary } from "@/types/siteReview";

export function getTotalFollowUpSignals(review: SiteReviewSummary): number {
	return (
		review.essentialDocuments.missingDocuments +
		review.essentialDocuments.pendingDocuments +
		review.essentialDocuments.expiredDocuments +
		review.protocolDeviations.openDeviations +
		review.icfVersionCheck.issueConsents
	);
}
