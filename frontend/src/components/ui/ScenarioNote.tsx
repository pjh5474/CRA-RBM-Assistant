import { type ReactNode } from "react";

interface ScenarioNoteProps {
	children: ReactNode;
}

export function ScenarioNote({ children }: ScenarioNoteProps) {
	return (
		<section className="rounded-2xl border border-indigo-200 bg-indigo-50 p-5">
			<h2 className="text-sm font-bold text-indigo-900">Scenario Note</h2>
			<p className="mt-2 text-sm leading-6 text-indigo-800">{children}</p>
		</section>
	);
}
