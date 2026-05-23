import { getDocumentStatusBadgeClass } from "@/lib/essentialDocument";
import { EssentialDocument } from "@/types/essentialDocument";

interface DocumentStatusBadgeProps {
	status: EssentialDocument["status"];
}

export function DocumentStatusBadge({ status }: DocumentStatusBadgeProps) {
	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${getDocumentStatusBadgeClass(status)}`}
		>
			{status}
		</span>
	);
}
