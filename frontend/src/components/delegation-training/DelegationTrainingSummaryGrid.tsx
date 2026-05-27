import { SummaryCard } from "@/components/ui/SummaryCard";
import { DelegationTrainingCheck } from "@/types/delegationTraining";

interface DelegationTrainingSummaryGridProps {
	check: DelegationTrainingCheck;
}

export function DelegationTrainingSummaryGrid({
	check,
}: DelegationTrainingSummaryGridProps) {
	return (
		<section className="grid gap-4 md:grid-cols-5">
			<SummaryCard title="Total Records" value={check.totalRecords} />
			<SummaryCard title="Valid" value={check.validRecords} />
			<SummaryCard title="Issues" value={check.issueRecords} />
			<SummaryCard
				title="Missing Training"
				value={check.missingTrainingRecords}
			/>
			<SummaryCard
				title="Training After Delegation"
				value={check.trainingAfterDelegationRecords}
			/>
		</section>
	);
}
