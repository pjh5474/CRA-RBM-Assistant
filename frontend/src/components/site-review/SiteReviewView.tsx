import { SiteReviewCraSummary } from "@/components/site-review/SiteReviewCraSummary";
import { SiteReviewHeader } from "@/components/site-review/SiteReviewHeader";
import { SiteReviewModules } from "@/components/site-review/SiteReviewModules";
import { SiteReviewSummaryGrid } from "@/components/site-review/SiteReviewSummaryGrid";
import { SiteStudyNav } from "@/components/layout/SiteStudyNav";
import { PortfolioPrototypeNotice } from "@/components/ui/PortfolioPrototypeNotice";
import { SiteReviewSummary } from "@/types/siteReview";

interface SiteReviewViewProps {
	review: SiteReviewSummary;
}

export function SiteReviewView({ review }: SiteReviewViewProps) {
	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<SiteStudyNav
					studyId={review.study.studyId}
					siteId={review.site.siteId}
				/>

				<SiteReviewHeader review={review} />

				<SiteReviewSummaryGrid review={review} />

				<SiteReviewCraSummary review={review} />

				<SiteReviewModules modules={review.modules} />

				<PortfolioPrototypeNotice>
					This Site Review Hub combines synthetic monitoring data, document
					readiness data, protocol deviation records, and ICF version checks to
					demonstrate CRA-oriented site review workflow. It is not intended for
					real clinical trial operation or regulatory submission.
				</PortfolioPrototypeNotice>
			</div>
		</main>
	);
}
