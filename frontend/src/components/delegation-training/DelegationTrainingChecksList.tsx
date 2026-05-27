import { DelegationTrainingCard } from "@/components/delegation-training/DelegationTrainingCard";
import { DelegationTrainingCheckItem } from "@/types/delegationTraining";

interface DelegationTrainingChecksListProps {
	checks: DelegationTrainingCheckItem[];
}

export function DelegationTrainingChecksList({
	checks,
}: DelegationTrainingChecksListProps) {
	return (
		<section className="space-y-5">
			<h2 className="text-lg font-bold text-slate-900">
				Delegation / Training Checks
			</h2>

			{checks.length === 0 ? (
				<div className="rounded-2xl border border-dashed border-slate-300 bg-white p-10 text-center">
					<h3 className="text-lg font-semibold text-slate-900">
						No delegation training records
					</h3>
					<p className="mt-2 text-sm text-slate-600">
						No delegation or training records were found for this site.
					</p>
				</div>
			) : (
				checks.map((item) => (
					<DelegationTrainingCard key={item.recordId} item={item} />
				))
			)}
		</section>
	);
}
