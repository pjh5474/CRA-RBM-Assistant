import { FindingCard } from "@/components/monitoring-report/FindingCard";
import { ReportSection } from "@/components/monitoring-report/ReportSection";
import { MonitoringReportFinding } from "@/types/monitoringReport";

interface MonitoringReportFindingsProps {
	findings: MonitoringReportFinding[];
}

export function MonitoringReportFindings({
	findings,
}: MonitoringReportFindingsProps) {
	return (
		<ReportSection title="Key Monitoring Findings">
			{findings.length === 0 ? (
				<p className="rounded-xl border border-dashed border-slate-300 p-6 text-sm text-slate-500">
					No major monitoring findings were generated for this site.
				</p>
			) : (
				<div className="space-y-4">
					{findings.map((finding, index) => (
						<FindingCard
							key={`${finding.category}-${index}`}
							finding={finding}
							index={index + 1}
						/>
					))}
				</div>
			)}
		</ReportSection>
	);
}
