import { DeviationInfoBlock } from "@/components/protocol-deviation/DeviationInfoBlock";
import { SeverityBadge } from "@/components/protocol-deviation/SeverityBadge";
import { StatusBadge } from "@/components/protocol-deviation/StatusBadge";
import { ProtocolDeviation } from "@/types/protocolDeviation";

interface DeviationCardProps {
	deviation: ProtocolDeviation;
}

export function DeviationCard({ deviation }: DeviationCardProps) {
	return (
		<article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<div className="mb-5 flex flex-wrap items-start justify-between gap-4">
				<div>
					<div className="mb-2 flex flex-wrap gap-2">
						<SeverityBadge severity={deviation.severity} />
						<StatusBadge status={deviation.status} />
						<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
							{deviation.category}
						</span>
					</div>

					<h2 className="text-lg font-bold text-slate-900">
						{deviation.description}
					</h2>

					<p className="mt-2 text-sm text-slate-500">{deviation.deviationId}</p>
				</div>
			</div>

			<div className="grid gap-4 md:grid-cols-2">
				<DeviationInfoBlock
					title="Subject Code"
					value={deviation.subjectCode ?? "N/A"}
				/>
				<DeviationInfoBlock
					title="Detected Date"
					value={deviation.detectedDate}
				/>
				<DeviationInfoBlock
					title="Root Cause"
					value={deviation.rootCause ?? "N/A"}
				/>
				<DeviationInfoBlock
					title="Corrective Action"
					value={deviation.correctiveAction ?? "N/A"}
				/>
				<DeviationInfoBlock
					title="Preventive Action"
					value={deviation.preventiveAction ?? "N/A"}
				/>
			</div>
		</article>
	);
}
