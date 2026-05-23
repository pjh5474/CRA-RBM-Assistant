interface DeviationInfoBlockProps {
	title: string;
	value: string;
}

export function DeviationInfoBlock({ title, value }: DeviationInfoBlockProps) {
	return (
		<div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
			<p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
				{title}
			</p>
			<p className="mt-2 text-sm leading-6 text-slate-800">{value}</p>
		</div>
	);
}
