import { DelegationTrainingCheckItem } from "@/types/delegationTraining";

export function getDelegationStatusBadgeClass(
	status: DelegationTrainingCheckItem["status"],
): string {
	return status === "Valid"
		? "bg-emerald-50 text-emerald-700"
		: "bg-red-50 text-red-700";
}
