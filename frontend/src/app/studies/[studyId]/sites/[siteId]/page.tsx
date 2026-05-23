import { SiteReviewView } from "@/components/site-review/SiteReviewView";
import { getSiteReviewSummary } from "@/lib/api";

interface SiteReviewPageProps {
	params: Promise<{
		studyId: string;
		siteId: string;
	}>;
}

export default async function SiteReviewPage({ params }: SiteReviewPageProps) {
	const { studyId, siteId } = await params;
	const review = await getSiteReviewSummary(studyId, siteId);

	return <SiteReviewView review={review} />;
}
