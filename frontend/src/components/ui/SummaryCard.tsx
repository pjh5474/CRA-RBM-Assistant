interface SummaryCardProps {
	title: string;
	value: number;
}

export function SummaryCard({ title, value }: SummaryCardProps) {
	return (
		<div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<p className="text-sm font-medium text-slate-500">{title}</p>
			<p className="mt-2 text-3xl font-bold text-slate-900">{value}</p>
		</div>
	);
}
