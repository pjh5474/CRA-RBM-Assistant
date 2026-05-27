import { getDelegationStatusBadgeClass } from "@/lib/delegationTraining";
import { DelegationTrainingCheckItem } from "@/types/delegationTraining";

interface DelegationStatusBadgeProps {
	status: DelegationTrainingCheckItem["status"];
}

export function DelegationStatusBadge({ status }: DelegationStatusBadgeProps) {
	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${getDelegationStatusBadgeClass(status)}`}
		>
			{status}
		</span>
	);
}
