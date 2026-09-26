"use client";

import { useState } from "react";
import { useQuery } from "@tanstack/react-query";

import {
	getConditionTrend,
	getCountryTrials,
	getTrialOverview,
	getYearlyTrials,
} from "@/lib/api";

import { OverviewCards } from "./OverviewCards";
import { YearlyTrialChart } from "./YearlyTrialChart";
import { CountryTrialChart } from "./CountryTrialChart";
import { ConditionTrendChart } from "./ConditionTrendChart";

export function ClinicalTrialDashboard() {
	const [condition, setCondition] = useState("Obesity");

	const overviewQuery = useQuery({
		queryKey: ["analytics", "overview"],
		queryFn: getTrialOverview,
	});

	const yearlyQuery = useQuery({
		queryKey: ["analytics", "yearly"],
		queryFn: getYearlyTrials,
	});

	const countryQuery = useQuery({
		queryKey: ["analytics", "countries", 15],
		queryFn: () => getCountryTrials(15),
	});

	const conditionQuery = useQuery({
		queryKey: ["analytics", "condition", condition],
		queryFn: () => getConditionTrend(condition),
	});

	const initialLoading =
		overviewQuery.isLoading || yearlyQuery.isLoading || countryQuery.isLoading;

	const initialError =
		overviewQuery.error || yearlyQuery.error || countryQuery.error;

	if (initialLoading) {
		return (
			<div className="py-20 text-center text-sm text-slate-500">
				Loading clinical trial analytics...
			</div>
		);
	}

	if (initialError) {
		return (
			<div className="rounded-xl border border-red-200 bg-red-50 p-5 text-sm text-red-700">
				Failed to load clinical trial analytics.
			</div>
		);
	}

	return (
		<div className="space-y-6">
			{overviewQuery.data && <OverviewCards data={overviewQuery.data} />}

			{yearlyQuery.data && <YearlyTrialChart data={yearlyQuery.data} />}

			{countryQuery.data && <CountryTrialChart data={countryQuery.data} />}

			<ConditionTrendChart
				condition={condition}
				data={conditionQuery.data ?? []}
				loading={conditionQuery.isFetching}
				onSearch={setCondition}
			/>
		</div>
	);
}
