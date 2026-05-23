import { type ReactNode } from "react";

interface ReportSectionProps {
	title: string;
	children: ReactNode;
}

export function ReportSection({ title, children }: ReportSectionProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="mb-4 text-lg font-bold text-slate-900">{title}</h2>
			{children}
		</section>
	);
}
