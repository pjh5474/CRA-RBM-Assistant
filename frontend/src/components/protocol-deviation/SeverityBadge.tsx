import { getSeverityBadgeClass } from "@/lib/protocolDeviation";
import { ProtocolDeviation } from "@/types/protocolDeviation";

interface SeverityBadgeProps {
	severity: ProtocolDeviation["severity"];
}

export function SeverityBadge({ severity }: SeverityBadgeProps) {
	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${getSeverityBadgeClass(severity)}`}
		>
			{severity}
		</span>
	);
}
