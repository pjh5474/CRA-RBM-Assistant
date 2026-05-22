import { ChecklistItem } from "@/types/checklist";

interface ChecklistPanelProps {
	title: string;
	items: ChecklistItem[];
}

export function ChecklistPanel({ title, items }: ChecklistPanelProps) {
	return (
		<div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="mb-4 text-xl font-bold text-slate-900">{title}</h2>

			<div className="space-y-4">
				{items.map((item, index) => (
					<div
						key={`${item.category}-${index}`}
						className="border-b pb-4 last:border-b-0"
					>
						<p className="mb-1 text-xs font-semibold text-blue-700">
							{item.category}
						</p>
						<p className="text-sm font-medium text-slate-900">{item.item}</p>
						<p className="mt-1 text-sm text-slate-600">{item.rationale}</p>
					</div>
				))}
			</div>
		</div>
	);
}
