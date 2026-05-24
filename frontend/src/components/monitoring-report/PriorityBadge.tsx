import { MonitoringReportFollowUpAction } from "@/types/monitoringReport";

export default function PriorityBadge({
	priority,
}: {
	priority: MonitoringReportFollowUpAction["priority"];
}) {
	const className =
		priority === "High"
			? "bg-red-50 text-red-700"
			: priority === "Medium"
				? "bg-amber-50 text-amber-700"
				: "bg-emerald-50 text-emerald-700";

	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${className}`}
		>
			{priority}
		</span>
	);
}
