import { RiskBadge } from "@/components/risk/RiskBadge";
import { InfoCard } from "@/components/ui/InfoCard";
import { SiteReviewSummary } from "@/types/siteReview";

interface SiteReviewHeaderProps {
	review: SiteReviewSummary;
}

export function SiteReviewHeader({ review }: SiteReviewHeaderProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<div className="mb-4 flex flex-wrap items-center gap-2">
				<RiskBadge level={review.site.riskLevel} />
				<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
					Risk Score: {review.site.riskScore}
				</span>
				<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
					{review.site.status}
				</span>
			</div>

			<p className="mb-2 text-sm font-semibold text-blue-700">Site Review Hub</p>

			<h1 className="text-2xl font-bold text-slate-900">{review.site.siteName}</h1>

			<p className="mt-2 text-sm text-slate-600">{review.study.title}</p>

			<div className="mt-6 grid gap-4 md:grid-cols-4">
				<InfoCard title="Site ID" value={review.site.siteId} />
				<InfoCard title="PI" value={review.site.principalInvestigator} />
				<InfoCard
					title="Enrollment"
					value={`${review.site.currentEnrollment} / ${review.site.targetEnrollment}`}
				/>
				<InfoCard title="Country" value={review.site.country} />
			</div>
		</section>
	);
}
