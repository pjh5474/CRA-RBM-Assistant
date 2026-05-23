import { type ReactNode } from "react";

interface PortfolioPrototypeNoticeProps {
	children: ReactNode;
}

export function PortfolioPrototypeNotice({
	children,
}: PortfolioPrototypeNoticeProps) {
	return (
		<section className="rounded-2xl border border-amber-200 bg-amber-50 p-5">
			<h2 className="text-sm font-bold text-amber-900">
				Portfolio Prototype Notice
			</h2>
			<p className="mt-2 text-sm leading-6 text-amber-800">{children}</p>
		</section>
	);
}
