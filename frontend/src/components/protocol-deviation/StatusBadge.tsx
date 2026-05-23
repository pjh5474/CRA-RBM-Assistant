import { getStatusBadgeClass } from "@/lib/protocolDeviation";
import { ProtocolDeviation } from "@/types/protocolDeviation";

interface StatusBadgeProps {
	status: ProtocolDeviation["status"];
}

export function StatusBadge({ status }: StatusBadgeProps) {
	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${getStatusBadgeClass(status)}`}
		>
			{status}
		</span>
	);
}
