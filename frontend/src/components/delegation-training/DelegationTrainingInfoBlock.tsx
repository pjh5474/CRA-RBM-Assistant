interface DelegationTrainingInfoBlockProps {
	title: string;
	value: string;
}

export function DelegationTrainingInfoBlock({
	title,
	value,
}: DelegationTrainingInfoBlockProps) {
	return (
		<div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
			<p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
				{title}
			</p>
			<p className="mt-2 text-sm leading-6 text-slate-800">{value}</p>
		</div>
	);
}
