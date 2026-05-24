import { MonitoringReportFollowUpAction } from "@/types/monitoringReport";
import PriorityBadge from "./PriorityBadge";

export default function FollowUpActionCard({
	action,
	index,
}: {
	action: MonitoringReportFollowUpAction;
	index: number;
}) {
	return (
		<article className="rounded-xl border border-slate-200 bg-slate-50 p-5">
			<div className="mb-3 flex flex-wrap items-center gap-2">
				<span className="rounded-full bg-slate-900 px-3 py-1 text-xs font-semibold text-white">
					Action {index}
				</span>
				<PriorityBadge priority={action.priority} />
				<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
					{action.category}
				</span>
			</div>

			<p className="text-sm leading-6 text-slate-800">{action.action}</p>
		</article>
	);
}
