import { RiskBadge } from "@/components/risk/RiskBadge";
import { RiskSite } from "@/types/risk";
import Link from "next/link";

interface RiskSitesTableProps {
	sites: RiskSite[];
}

export function RiskSitesTable({ sites }: RiskSitesTableProps) {
	return (
		<section className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
			<div className="border-b border-slate-200 p-5">
				<h2 className="text-lg font-bold text-slate-900">Site Risk Overview</h2>
			</div>

			<div className="overflow-x-auto">
				<table className="w-full min-w-[900px] text-left text-sm">
					<thead className="bg-slate-50 text-xs uppercase tracking-wide text-slate-500">
						<tr>
							<th className="px-5 py-3">Site</th>
							<th className="px-5 py-3">PI</th>
							<th className="px-5 py-3">Enrollment</th>
							<th className="px-5 py-3">Risk Score</th>
							<th className="px-5 py-3">Risk Level</th>
							<th className="px-5 py-3">Risk Factors</th>
							<th className="px-5 py-3">Actions</th>
						</tr>
					</thead>
					<tbody className="divide-y divide-slate-100">
						{sites.map((site) => (
							<tr key={site.siteId} className="align-top">
								<td className="px-5 py-4">
									<p className="font-semibold text-slate-900">
										{site.siteName}
									</p>
									<p className="text-xs text-slate-500">{site.siteId}</p>
								</td>
								<td className="px-5 py-4 text-slate-700">
									{site.principalInvestigator}
								</td>
								<td className="px-5 py-4 text-slate-700">
									{site.currentEnrollment} / {site.targetEnrollment}
								</td>
								<td className="px-5 py-4 font-semibold text-slate-900">
									{site.riskScore}
								</td>
								<td className="px-5 py-4">
									<RiskBadge level={site.riskLevel} />
								</td>
								<td className="px-5 py-4">
									{site.riskFactors.length === 0 ? (
										<span className="text-slate-400">No major risk factor</span>
									) : (
										<ul className="space-y-1">
											{site.riskFactors.map((factor) => (
												<li key={factor} className="text-slate-700">
													- {factor}
												</li>
											))}
										</ul>
									)}
								</td>
								<td className="px-5 py-4">
									<Link
										href={`/studies/${site.studyId}/sites/${site.siteId}`}
										className="inline-flex rounded-lg bg-slate-900 px-3 py-2 text-xs font-semibold text-white hover:bg-slate-800"
									>
										Open Site Review
									</Link>
								</td>
							</tr>
						))}
					</tbody>
				</table>
			</div>
		</section>
	);
}
