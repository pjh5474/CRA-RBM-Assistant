"use client";

import {
	CartesianGrid,
	Line,
	LineChart,
	ResponsiveContainer,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

import type { YearlyTrial } from "@/types/analytics";

type Props = {
	data: YearlyTrial[];
};

export function YearlyTrialChart({ data }: Props) {
	return (
		<section className="rounded-xl border bg-white p-5 shadow-sm">
			<div className="mb-5">
				<h2 className="text-lg font-semibold">Trials by Start Year</h2>

				<p className="mt-1 text-sm text-slate-500">
					Number of registered studies grouped by study start year.
				</p>
			</div>

			<div className="h-90">
				<ResponsiveContainer width="100%" height="100%">
					<LineChart data={data}>
						<CartesianGrid strokeDasharray="3 3" />

						<XAxis dataKey="study_year" minTickGap={30} />

						<YAxis />

						<Tooltip formatter={(value) => Number(value).toLocaleString()} />

						<Line
							type="monotone"
							dataKey="trial_count"
							stroke="currentColor"
							strokeWidth={2}
							dot={false}
						/>
					</LineChart>
				</ResponsiveContainer>
			</div>
		</section>
	);
}
