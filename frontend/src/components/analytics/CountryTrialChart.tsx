"use client";

import {
	Bar,
	BarChart,
	CartesianGrid,
	ResponsiveContainer,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

import type { CountryTrial } from "@/types/analytics";

type Props = {
	data: CountryTrial[];
};

export function CountryTrialChart({ data }: Props) {
	return (
		<section className="rounded-xl border bg-white p-5 shadow-sm">
			<div className="mb-5">
				<h2 className="text-lg font-semibold">Trials by Country</h2>

				<p className="mt-1 text-sm text-slate-500">
					Top countries by distinct registered trials.
				</p>
			</div>

			<div className="h-105">
				<ResponsiveContainer width="100%" height="100%">
					<BarChart
						data={data}
						layout="vertical"
						margin={{
							left: 40,
							right: 20,
						}}
					>
						<CartesianGrid strokeDasharray="3 3" />

						<XAxis type="number" />

						<YAxis type="category" dataKey="country" width={110} />

						<Tooltip formatter={(value) => Number(value).toLocaleString()} />

						<Bar dataKey="trial_count" fill="currentColor" />
					</BarChart>
				</ResponsiveContainer>
			</div>
		</section>
	);
}
