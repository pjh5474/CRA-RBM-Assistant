import { BackLink } from "@/components/layout/BackLink";
import { PageContainer } from "@/components/layout/PageContainer";
import { RiskSitesTable } from "@/components/risk/RiskSitesTable";
import { SummaryCard } from "@/components/ui/SummaryCard";
import { getStudyDetail, getStudyRiskSites } from "@/lib/api";
import { getRiskLevelCounts } from "@/lib/risk";

interface RiskDashboardPageProps {
	params: Promise<{
		studyId: string;
	}>;
}

export default async function RiskDashboardPage({
	params,
}: RiskDashboardPageProps) {
	const { studyId } = await params;

	const [study, riskSites] = await Promise.all([
		getStudyDetail(studyId),
		getStudyRiskSites(studyId),
	]);

	const { high, medium, low } = getRiskLevelCounts(riskSites);

	return (
		<PageContainer className="space-y-8">
			<div>
				<BackLink href={`/studies/${study.studyId}`}>
					← Back to study overview
				</BackLink>
			</div>

			<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
				<p className="mb-2 text-sm font-semibold text-blue-700">
					Site Risk Dashboard
				</p>
				<h1 className="text-2xl font-bold text-slate-900">{study.title}</h1>
				<p className="mt-2 text-sm text-slate-600">
					Site-level risk indicators are calculated using synthetic monitoring
					data for portfolio demonstration.
				</p>
			</section>

			<section className="grid gap-4 md:grid-cols-3">
				<SummaryCard title="High Risk Sites" value={high} />
				<SummaryCard title="Medium Risk Sites" value={medium} />
				<SummaryCard title="Low Risk Sites" value={low} />
			</section>

			<RiskSitesTable sites={riskSites} />
		</PageContainer>
	);
}
