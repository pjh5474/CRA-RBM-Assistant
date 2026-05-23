import { DeviationCard } from "@/components/protocol-deviation/DeviationCard";
import { ProtocolDeviation } from "@/types/protocolDeviation";

interface ProtocolDeviationsListProps {
	deviations: ProtocolDeviation[];
}

export function ProtocolDeviationsList({
	deviations,
}: ProtocolDeviationsListProps) {
	return (
		<section className="space-y-5">
			{deviations.length === 0 ? (
				<div className="rounded-2xl border border-dashed border-slate-300 bg-white p-10 text-center">
					<h2 className="text-lg font-semibold text-slate-900">
						No protocol deviations
					</h2>
					<p className="mt-2 text-sm text-slate-600">
						No protocol deviation records were found for this site.
					</p>
				</div>
			) : (
				deviations.map((deviation) => (
					<DeviationCard
						key={deviation.deviationId}
						deviation={deviation}
					/>
				))
			)}
		</section>
	);
}
