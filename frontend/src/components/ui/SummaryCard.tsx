interface SummaryCardProps {
	title: string;
	value: string | number;
	emphasis?: boolean;
}

export function SummaryCard({
	title,
	value,
	emphasis = false,
}: SummaryCardProps) {
	return (
		<div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
			<p className="text-sm font-medium text-slate-500">{title}</p>
			<p
				className={`mt-2 text-2xl font-bold ${
					emphasis ? "text-blue-700" : "text-slate-900"
				}`}
			>
				{value}
			</p>
		</div>
	);
}
