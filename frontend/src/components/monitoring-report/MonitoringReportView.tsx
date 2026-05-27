import { MonitoringReportFindings } from "@/components/monitoring-report/MonitoringReportFindings";
import { MonitoringReportHeader } from "@/components/monitoring-report/MonitoringReportHeader";
import { ReportSection } from "@/components/monitoring-report/ReportSection";
import { SiteStudyNav } from "@/components/layout/SiteStudyNav";
import { PortfolioPrototypeNotice } from "@/components/ui/PortfolioPrototypeNotice";
import { MonitoringReportDraft } from "@/types/monitoringReport";
import { SummaryCard } from "../ui/SummaryCard";
import ReviewSummaryCard from "./ReviewSummaryCard";
import { FindingCard } from "./FindingCard";
import FollowUpActionCard from "./FollowUpActionCard";

interface MonitoringReportViewProps {
	report: MonitoringReportDraft;
}

export function MonitoringReportView({ report }: MonitoringReportViewProps) {
	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<SiteStudyNav studyId={report.studyId} siteId={report.siteId} />

				<MonitoringReportHeader report={report} />

				<section className="grid gap-4 md:grid-cols-5">
					<SummaryCard
						title="Document Readiness"
						value={`${report.essentialDocumentSummary.readinessScore}%`}
					/>
					<SummaryCard
						title="Open Deviations"
						value={report.protocolDeviationSummary.openDeviations}
					/>
					<SummaryCard
						title="ICF Issues"
						value={report.icfSummary.issueConsents}
					/>
					<SummaryCard
						title="Training Issues"
						value={report.delegationTrainingSummary.issueRecords}
					/>
					<SummaryCard
						title="Follow-up Actions"
						value={report.followUpActions.length}
					/>
				</section>

				<ReportSection title="Executive Summary">
					<p className="text-sm leading-7 text-slate-700">{report.summary}</p>
				</ReportSection>

				<ReportSection title="Integrated Review Summary">
					<div className="grid gap-4 md:grid-cols-2">
						<ReviewSummaryCard
							title="Risk Summary"
							items={[
								`Risk level: ${report.riskSummary.riskLevel}`,
								`Risk score: ${report.riskSummary.riskScore}`,
								`Risk factors: ${
									report.riskSummary.riskFactors.length > 0
										? report.riskSummary.riskFactors.join(", ")
										: "No major risk factor"
								}`,
							]}
						/>
						<ReviewSummaryCard
							title="Essential Documents"
							items={[
								`Readiness score: ${report.essentialDocumentSummary.readinessScore}%`,
								`Ready: ${report.essentialDocumentSummary.readyDocuments}`,
								`Missing: ${report.essentialDocumentSummary.missingDocuments}`,
								`Pending: ${report.essentialDocumentSummary.pendingDocuments}`,
								`Expired: ${report.essentialDocumentSummary.expiredDocuments}`,
							]}
						/>
						<ReviewSummaryCard
							title="Protocol Deviations"
							items={[
								`Total deviations: ${report.protocolDeviationSummary.totalDeviations}`,
								`Open: ${report.protocolDeviationSummary.openDeviations}`,
								`In review: ${report.protocolDeviationSummary.inReviewDeviations}`,
								`Major: ${report.protocolDeviationSummary.majorDeviations}`,
								`Critical: ${report.protocolDeviationSummary.criticalDeviations}`,
							]}
						/>
						<ReviewSummaryCard
							title="ICF Version Check"
							items={[
								`Total consents: ${report.icfSummary.totalConsents}`,
								`Valid consents: ${report.icfSummary.validConsents}`,
								`Issue consents: ${report.icfSummary.issueConsents}`,
							]}
						/>
						<ReviewSummaryCard
							title="Delegation & Training"
							items={[
								`Total records: ${report.delegationTrainingSummary.totalRecords}`,
								`Valid records: ${report.delegationTrainingSummary.validRecords}`,
								`Issue records: ${report.delegationTrainingSummary.issueRecords}`,
								`Missing training: ${report.delegationTrainingSummary.missingTrainingRecords}`,
								`Training after delegation: ${report.delegationTrainingSummary.trainingAfterDelegationRecords}`,
							]}
						/>
					</div>
				</ReportSection>

				<ReportSection title="Key Monitoring Findings">
					{report.findings.length === 0 ? (
						<p className="rounded-xl border border-dashed border-slate-300 p-6 text-sm text-slate-500">
							No major monitoring findings were generated for this site.
						</p>
					) : (
						<div className="space-y-4">
							{report.findings.map((finding, index) => (
								<FindingCard
									key={`${finding.category}-${index}`}
									finding={finding}
									index={index + 1}
								/>
							))}
						</div>
					)}
				</ReportSection>

				<ReportSection title="CRA Follow-up Action Plan">
					{report.followUpActions.length === 0 ? (
						<p className="rounded-xl border border-dashed border-slate-300 p-6 text-sm text-slate-500">
							No follow-up action was generated for this site.
						</p>
					) : (
						<div className="space-y-4">
							{report.followUpActions.map((action, index) => (
								<FollowUpActionCard
									key={`${action.category}-${index}`}
									action={action}
									index={index + 1}
								/>
							))}
						</div>
					)}
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
