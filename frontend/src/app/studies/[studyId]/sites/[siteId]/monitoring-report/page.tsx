import Link from "next/link";
import { getMonitoringReportDraft } from "@/lib/api";
import { MonitoringReportDraft } from "@/types/monitoringReport";

interface MonitoringReportPageProps {
	params: Promise<{
		studyId: string;
		siteId: string;
	}>;
}

export default async function MonitoringReportPage({
	params,
}: MonitoringReportPageProps) {
	const { studyId, siteId } = await params;
	const report = await getMonitoringReportDraft(studyId, siteId);

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-5xl space-y-8">
				<div className="flex flex-wrap gap-4">
					<Link
						href={`/studies/${report.studyId}/risk-dashboard`}
						className="text-sm font-medium text-blue-700 hover:text-blue-800"
					>
						← Back to risk dashboard
					</Link>

					<Link
						href={`/studies/${report.studyId}`}
						className="text-sm font-medium text-blue-700 hover:text-blue-800"
					>
						Back to study overview
					</Link>
				</div>

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

					<h1 className="text-2xl font-bold text-slate-900">
						{report.siteName}
					</h1>

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

				<ReportSection title="Executive Summary">
					<p className="text-sm leading-7 text-slate-700">{report.summary}</p>
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

				<ReportSection title="Limitations">
					<ul className="space-y-2">
						{report.limitations.map((limitation) => (
							<li key={limitation} className="text-sm leading-6 text-slate-700">
								- {limitation}
							</li>
						))}
					</ul>
				</ReportSection>

				<section className="rounded-2xl border border-amber-200 bg-amber-50 p-5">
					<h2 className="text-sm font-bold text-amber-900">
						Portfolio Prototype Notice
					</h2>
					<p className="mt-2 text-sm leading-6 text-amber-800">
						This draft is generated from synthetic monitoring data and
						simplified rule-based logic. It is intended to demonstrate
						CRA-oriented documentation support and does not replace
						sponsor-approved monitoring report templates or CRA judgment.
					</p>
				</section>
			</div>
		</main>
	);
}

function ReportSection({
	title,
	children,
}: {
	title: string;
	children: React.ReactNode;
}) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="mb-4 text-lg font-bold text-slate-900">{title}</h2>
			{children}
		</section>
	);
}

function FindingCard({
	finding,
	index,
}: {
	finding: MonitoringReportDraft["findings"][number];
	index: number;
}) {
	return (
		<article className="rounded-xl border border-slate-200 bg-slate-50 p-5">
			<div className="mb-3 flex flex-wrap items-center gap-2">
				<span className="rounded-full bg-slate-900 px-3 py-1 text-xs font-semibold text-white">
					Finding {index}
				</span>
				<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
					{finding.category}
				</span>
			</div>

			<div className="space-y-4">
				<div>
					<p className="mb-1 text-xs font-semibold uppercase tracking-wide text-slate-500">
						Finding
					</p>
					<p className="text-sm leading-6 text-slate-800">{finding.finding}</p>
				</div>

				<div>
					<p className="mb-1 text-xs font-semibold uppercase tracking-wide text-slate-500">
						Recommended CRA Follow-up
					</p>
					<p className="text-sm leading-6 text-slate-800">
						{finding.recommendedAction}
					</p>
				</div>
			</div>
		</article>
	);
}

function InfoCard({ title, value }: { title: string; value: string }) {
	return (
		<div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
			<p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
				{title}
			</p>
			<p className="mt-2 text-sm font-medium text-slate-900">{value}</p>
		</div>
	);
}

function RiskBadge({ level }: { level: MonitoringReportDraft["riskLevel"] }) {
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
