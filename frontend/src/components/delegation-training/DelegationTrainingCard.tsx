import { DelegationTrainingInfoBlock } from "@/components/delegation-training/DelegationTrainingInfoBlock";
import { DelegationStatusBadge } from "@/components/delegation-training/DelegationStatusBadge";
import { DelegationTrainingCheckItem } from "@/types/delegationTraining";

interface DelegationTrainingCardProps {
	item: DelegationTrainingCheckItem;
}

export function DelegationTrainingCard({ item }: DelegationTrainingCardProps) {
	return (
		<article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<div className="mb-5 flex flex-wrap items-start justify-between gap-4">
				<div>
					<div className="mb-2 flex flex-wrap gap-2">
						<DelegationStatusBadge status={item.status} />
						{item.issueType && (
							<span className="rounded-full bg-red-50 px-3 py-1 text-xs font-semibold text-red-700">
								{item.issueType}
							</span>
						)}
						<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
							{item.trainingStatus}
						</span>
					</div>

					<h2 className="text-lg font-bold text-slate-900">{item.staffName}</h2>

					<p className="mt-1 text-sm text-slate-600">{item.role}</p>
					<p className="mt-2 text-sm text-slate-500">{item.recordId}</p>
				</div>
			</div>

			<div className="grid gap-4 md:grid-cols-2">
				<DelegationTrainingInfoBlock
					title="Delegated Task"
					value={item.delegatedTask}
				/>
				<DelegationTrainingInfoBlock
					title="Delegation Start Date"
					value={item.delegationStartDate}
				/>
				<DelegationTrainingInfoBlock
					title="GCP Training Date"
					value={item.gcpTrainingDate ?? "N/A"}
				/>
				<DelegationTrainingInfoBlock
					title="Protocol Training Date"
					value={item.protocolTrainingDate ?? "N/A"}
				/>
				<DelegationTrainingInfoBlock title="Review Message" value={item.message} />
			</div>
		</article>
	);
}
