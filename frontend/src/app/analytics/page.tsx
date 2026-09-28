import Link from "next/link";
import { ClinicalTrialDashboard } from "@/components/analytics/ClinicalTrialDashboard";

export default function AnalyticsPage() {
	return (
		<main className="mx-auto w-full max-w-7xl px-6 py-8">
			<div className="mb-6">
				<Link
					href="/"
					className="text-sm font-medium text-blue-700 hover:text-blue-800"
				>
					← Back to study list
				</Link>
			</div>

			<header className="mb-8">
				<p className="text-sm font-medium text-slate-500">
					Clinical Trial Data Platform
				</p>

				<h1 className="mt-2 text-3xl font-semibold tracking-tight">
					Clinical Trial Landscape
				</h1>

				<p className="mt-3 max-w-3xl text-sm leading-6 text-slate-600">
					Explore ClinicalTrials.gov registry data processed through the CRA-RBM
					clinical trial data platform.
				</p>
			</header>

			<ClinicalTrialDashboard />
		</main>
	);
}
