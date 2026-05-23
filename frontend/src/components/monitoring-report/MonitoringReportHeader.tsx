import { InfoCard } from "@/components/ui/InfoCard";
import { RiskBadge } from "@/components/risk/RiskBadge";
import { MonitoringReportDraft } from "@/types/monitoringReport";

interface MonitoringReportHeaderProps {
	report: MonitoringReportDraft;
}

export function MonitoringReportHeader({ report }: MonitoringReportHeaderProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<div className="mb-4 flex flex-wrap items-center gap-2">
				<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
					{report.visitType}
				</span>
				<RiskBadge level={report.riskLevel} />
				<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
					Risk Score: {report.riskScore}
				</span>
			</div>

			<p className="mb-2 text-sm font-semibold text-blue-700">
				Monitoring Visit Report Draft
			</p>

			<h1 className="text-2xl font-bold text-slate-900">{report.siteName}</h1>

			<p className="mt-2 text-sm text-slate-600">{report.studyTitle}</p>

			<div className="mt-6 grid gap-4 md:grid-cols-3">
				<InfoCard title="Study ID" value={report.studyId} />
				<InfoCard title="Site ID" value={report.siteId} />
				<InfoCard
					title="Principal Investigator"
					value={report.principalInvestigator}
				/>
			</div>
		</section>
	);
}
