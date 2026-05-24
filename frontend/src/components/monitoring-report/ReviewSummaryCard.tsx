export default function ReviewSummaryCard({
	title,
	items,
}: {
	title: string;
	items: string[];
}) {
	return (
		<div className="rounded-xl border border-slate-200 bg-slate-50 p-5">
			<h3 className="mb-3 text-sm font-bold text-slate-900">{title}</h3>
			<ul className="space-y-2">
				{items.map((item) => (
					<li key={item} className="text-sm leading-6 text-slate-700">
						- {item}
					</li>
				))}
			</ul>
		</div>
	);
}
