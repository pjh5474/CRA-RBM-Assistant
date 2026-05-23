import { MonitoringReportFindings } from "@/components/monitoring-report/MonitoringReportFindings";
import { MonitoringReportHeader } from "@/components/monitoring-report/MonitoringReportHeader";
import { ReportSection } from "@/components/monitoring-report/ReportSection";
import { SiteStudyNav } from "@/components/layout/SiteStudyNav";
import { PortfolioPrototypeNotice } from "@/components/ui/PortfolioPrototypeNotice";
import { MonitoringReportDraft } from "@/types/monitoringReport";

interface MonitoringReportViewProps {
	report: MonitoringReportDraft;
}

export function MonitoringReportView({ report }: MonitoringReportViewProps) {
	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-5xl space-y-8">
				<SiteStudyNav studyId={report.studyId} />

				<MonitoringReportHeader report={report} />

				<ReportSection title="Executive Summary">
					<p className="text-sm leading-7 text-slate-700">{report.summary}</p>
				</ReportSection>

				<MonitoringReportFindings findings={report.findings} />

				<ReportSection title="Limitations">
					<ul className="space-y-2">
						{report.limitations.map((limitation) => (
							<li key={limitation} className="text-sm leading-6 text-slate-700">
								- {limitation}
							</li>
						))}
					</ul>
				</ReportSection>

				<PortfolioPrototypeNotice>
					This draft is generated from synthetic monitoring data and simplified
					rule-based logic. It is intended to demonstrate CRA-oriented
					documentation support and does not replace sponsor-approved monitoring
					report templates or CRA judgment.
				</PortfolioPrototypeNotice>
			</div>
		</main>
	);
}
