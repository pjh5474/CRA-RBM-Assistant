import type { TrialOverview } from "@/types/analytics";

type Props = {
	data: TrialOverview;
};

function formatNumber(value: number) {
	return new Intl.NumberFormat("en-US").format(value);
}

export function OverviewCards({ data }: Props) {
	const cards = [
		{
			label: "Trials with Start Year",
			value: formatNumber(data.total_trials),
		},
		{
			label: "Interventional",
			value: formatNumber(data.interventional_trials),
		},
		{
			label: "Observational",
			value: formatNumber(data.observational_trials),
		},
		{
			label: "Other",
			value: formatNumber(data.other_trials),
		},
	];

	return (
		<section className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
			{cards.map((card) => (
				<div
					key={card.label}
					className="rounded-xl border bg-white p-5 shadow-sm"
				>
					<p className="text-sm text-slate-500">{card.label}</p>

					<p className="mt-2 text-3xl font-semibold tracking-tight">
						{card.value}
					</p>
				</div>
			))}
		</section>
	);
}
