import { getReadinessBarWidth } from "@/lib/essentialDocument";

interface ReadinessBarProps {
	readinessScore: number;
}

export function ReadinessBar({ readinessScore }: ReadinessBarProps) {
	const barWidth = getReadinessBarWidth(readinessScore);

	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<div className="mb-3 flex items-center justify-between">
				<h2 className="text-lg font-bold text-slate-900">
					Document Readiness Score
				</h2>
				<span className="text-sm font-semibold text-slate-700">
					{readinessScore}%
				</span>
			</div>

			<div className="h-3 rounded-full bg-slate-100">
				<div
					className="h-3 rounded-full bg-blue-700"
					style={{ width: `${barWidth}%` }}
				/>
			</div>
		</section>
	);
}
