import Link from "next/link";
import { getStudyActionItems, getStudyDetail } from "@/lib/api";

interface ActionItemsPageProps {
	params: Promise<{
		studyId: string;
	}>;
}

export default async function ActionItemsPage({
	params,
}: ActionItemsPageProps) {
	const { studyId } = await params;

	const [study, siteActionItems] = await Promise.all([
		getStudyDetail(studyId),
		getStudyActionItems(studyId),
	]);

	const totalSitesWithActions = siteActionItems.length;
	const totalActionItems = siteActionItems.reduce(
		(sum, site) => sum + site.actionItems.length,
		0,
	);
	const highRiskSites = siteActionItems.filter(
		(site) => site.riskLevel === "High",
	).length;

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<div className="flex flex-wrap items-center gap-4">
					<Link
						href={`/studies/${study.studyId}`}
						className="text-sm font-medium text-blue-700 hover:text-blue-800"
					>
						← Back to study overview
					</Link>

					<Link
						href={`/studies/${study.studyId}/risk-dashboard`}
						className="text-sm font-medium text-blue-700 hover:text-blue-800"
					>
						View risk dashboard →
					</Link>
				</div>

				<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
					<p className="mb-2 text-sm font-semibold text-blue-700">
						CRA Follow-up Action Items
					</p>

					<h1 className="text-2xl font-bold text-slate-900">{study.title}</h1>

					<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
						This page translates site-level risk factors into CRA-oriented
						follow-up action items. The recommendations are generated from
						simplified rule-based logic using synthetic monitoring data.
					</p>
				</section>

				<section className="grid gap-4 md:grid-cols-3">
					<SummaryCard
						title="Sites Requiring Follow-up"
						value={totalSitesWithActions}
					/>
					<SummaryCard title="Total Action Items" value={totalActionItems} />
					<SummaryCard title="High Risk Sites" value={highRiskSites} />
				</section>

				<section className="space-y-5">
					{siteActionItems.length === 0 ? (
						<EmptyState />
					) : (
						siteActionItems.map((site) => (
							<SiteActionItemCard key={site.siteId} site={site} />
						))
					)}
				</section>
			</div>
		</main>
	);
}

function SummaryCard({ title, value }: { title: string; value: number }) {
	return (
		<div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<p className="text-sm font-medium text-slate-500">{title}</p>
			<p className="mt-2 text-3xl font-bold text-slate-900">{value}</p>
		</div>
	);
}

function SiteActionItemCard({
	site,
}: {
	site: {
		siteId: string;
		studyId: string;
		siteName: string;
		riskScore: number;
		riskLevel: "Low" | "Medium" | "High";
		actionItems: Array<{
			riskFactor: string;
			recommendedAction: string;
		}>;
	};
}) {
	return (
		<article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<div className="mb-5 flex flex-wrap items-start justify-between gap-4">
				<div>
					<div className="mb-2 flex flex-wrap items-center gap-2">
						<RiskBadge level={site.riskLevel} />
						<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
							Risk Score: {site.riskScore}
						</span>
					</div>

					<h2 className="text-xl font-bold text-slate-900">{site.siteName}</h2>
					<p className="mt-1 text-sm text-slate-500">{site.siteId}</p>
				</div>
			</div>

			<div className="space-y-4">
				{site.actionItems.map((actionItem, index) => (
					<div
						key={`${site.siteId}-${actionItem.riskFactor}-${index}`}
						className="rounded-xl border border-slate-200 bg-slate-50 p-4"
					>
						<p className="mb-1 text-xs font-semibold uppercase tracking-wide text-blue-700">
							Risk Factor
						</p>
						<p className="font-medium text-slate-900">
							{actionItem.riskFactor}
						</p>

						<p className="mt-3 mb-1 text-xs font-semibold uppercase tracking-wide text-slate-500">
							Recommended CRA Action
						</p>
						<p className="text-sm leading-6 text-slate-700">
							{actionItem.recommendedAction}
						</p>
					</div>
				))}
			</div>
		</article>
	);
}

function RiskBadge({ level }: { level: "Low" | "Medium" | "High" }) {
	const className =
		level === "High"
			? "bg-red-50 text-red-700"
			: level === "Medium"
				? "bg-amber-50 text-amber-700"
				: "bg-emerald-50 text-emerald-700";

	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${className}`}
		>
			{level}
		</span>
	);
}

function EmptyState() {
	return (
		<div className="rounded-2xl border border-dashed border-slate-300 bg-white p-10 text-center">
			<h2 className="text-lg font-semibold text-slate-900">
				No follow-up action items
			</h2>
			<p className="mt-2 text-sm text-slate-600">
				No medium or high risk sites were detected for this study.
			</p>
		</div>
	);
}
