import { EssentialDocumentReadiness } from "@/types/essentialDocument";

export function getDocumentIssueCount(
	readiness: EssentialDocumentReadiness,
): number {
	return (
		readiness.missingDocuments +
		readiness.pendingDocuments +
		readiness.expiredDocuments
	);
}

export function getReadinessBarWidth(readinessScore: number): number {
	return Math.min(readinessScore, 100);
}

export function getDocumentStatusBadgeClass(
	status: EssentialDocumentReadiness["documents"][number]["status"],
): string {
	switch (status) {
		case "Ready":
			return "bg-emerald-50 text-emerald-700";
		case "Missing":
			return "bg-red-50 text-red-700";
		case "Expired":
			return "bg-orange-50 text-orange-700";
		default:
			return "bg-amber-50 text-amber-700";
	}
}
