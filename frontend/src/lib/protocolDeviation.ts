import { ProtocolDeviation } from "@/types/protocolDeviation";

export function getSeverityBadgeClass(
	severity: ProtocolDeviation["severity"],
): string {
	switch (severity) {
		case "Critical":
			return "bg-red-50 text-red-700";
		case "Major":
			return "bg-orange-50 text-orange-700";
		default:
			return "bg-blue-50 text-blue-700";
	}
}

export function getStatusBadgeClass(
	status: ProtocolDeviation["status"],
): string {
	switch (status) {
		case "Open":
			return "bg-red-50 text-red-700";
		case "In Review":
			return "bg-amber-50 text-amber-700";
		default:
			return "bg-emerald-50 text-emerald-700";
	}
}
