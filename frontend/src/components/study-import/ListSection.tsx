interface ListSectionProps {
	title: string;
	items: string[];
}

export function ListSection({ title, items }: ListSectionProps) {
	return (
		<section>
			<h4 className="mb-2 text-sm font-bold text-slate-900">{title}</h4>
			{items.length === 0 ? (
				<p className="rounded-xl bg-slate-50 p-4 text-sm text-slate-500">
					Not available
				</p>
			) : (
				<ul className="space-y-2 rounded-xl bg-slate-50 p-4">
					{items.map((item, index) => (
						<li
							key={`${title}-${index}`}
							className="text-sm leading-6 text-slate-700"
						>
							- {item}
						</li>
					))}
				</ul>
			)}
		</section>
	);
}
