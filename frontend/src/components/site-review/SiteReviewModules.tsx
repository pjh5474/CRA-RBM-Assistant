import Link from "next/link";
import { SiteReviewModule } from "@/types/siteReview";

interface SiteReviewModulesProps {
	modules: SiteReviewModule[];
}

export function SiteReviewModules({ modules }: SiteReviewModulesProps) {
	return (
		<section>
			<h2 className="mb-4 text-lg font-bold text-slate-900">Review Modules</h2>

			<div className="grid gap-4 md:grid-cols-2">
				{modules.map((module) => (
					<Link
						key={module.href}
						href={module.href}
						className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-md"
					>
						<div className="mb-3 flex flex-wrap items-center justify-between gap-2">
							<h3 className="text-lg font-bold text-slate-900">
								{module.title}
							</h3>
							<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
								{module.statusLabel}
							</span>
						</div>

						<p className="text-sm leading-6 text-slate-600">
							{module.description}
						</p>
					</Link>
				))}
			</div>
		</section>
	);
}
