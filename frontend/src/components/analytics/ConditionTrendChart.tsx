"use client";

import { FormEvent, useState } from "react";
import {
	CartesianGrid,
	Legend,
	Line,
	LineChart,
	ResponsiveContainer,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

import type { ConditionTrend } from "@/types/analytics";

type Props = {
	condition: string;
	data: ConditionTrend[];
	onSearch: (condition: string) => void;
	loading?: boolean;
};

export function ConditionTrendChart({
	condition,
	data,
	onSearch,
	loading = false,
}: Props) {
	const [input, setInput] = useState(condition);

	function handleSubmit(event: FormEvent) {
		event.preventDefault();

		const value = input.trim();

		if (!value) {
			return;
		}

		onSearch(value);
	}

	return (
		<section className="rounded-xl border bg-white p-5 shadow-sm">
			<div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
				<div>
					<h2 className="text-lg font-semibold">Condition Trend</h2>

					<p className="mt-1 text-sm text-slate-500">
						Compare yearly study activity for a clinical condition.
					</p>
				</div>

				<form onSubmit={handleSubmit} className="flex gap-2">
					<input
						value={input}
						onChange={(event) => setInput(event.target.value)}
						placeholder="e.g. Obesity"
						className="h-10 w-56 rounded-md border px-3 text-sm outline-none focus:ring-2"
					/>

					<button
						type="submit"
						disabled={loading}
						className="h-10 rounded-md bg-slate-900 px-4 text-sm font-medium text-white disabled:opacity-50"
					>
						{loading ? "Loading..." : "Search"}
					</button>
				</form>
			</div>

			<div className="mt-6 h-90">
				{data.length === 0 ? (
					<div className="flex h-full items-center justify-center text-sm text-slate-500">
						No trend data found for {condition}.
					</div>
				) : (
					<ResponsiveContainer width="100%" height="100%">
						<LineChart data={data}>
							<CartesianGrid strokeDasharray="3 3" />

							<XAxis dataKey="study_year" minTickGap={30} />

							<YAxis />

							<Tooltip formatter={(value) => Number(value).toLocaleString()} />

							<Legend />

							<Line
								type="monotone"
								dataKey="trial_count"
								name="Total"
								stroke="currentColor"
								strokeWidth={2}
								dot={false}
							/>

							<Line
								type="monotone"
								dataKey="interventional_count"
								name="Interventional"
								stroke="currentColor"
								strokeWidth={1}
								strokeDasharray="5 5"
								dot={false}
							/>

							<Line
								type="monotone"
								dataKey="observational_count"
								name="Observational"
								stroke="currentColor"
								strokeWidth={1}
								strokeDasharray="2 4"
								dot={false}
							/>
						</LineChart>
					</ResponsiveContainer>
				)}
			</div>
		</section>
	);
}
