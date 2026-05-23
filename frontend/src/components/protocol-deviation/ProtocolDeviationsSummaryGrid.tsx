import { SummaryCard } from "@/components/ui/SummaryCard";
import { ProtocolDeviationSummary } from "@/types/protocolDeviation";

interface ProtocolDeviationsSummaryGridProps {
	summary: ProtocolDeviationSummary;
}

export function ProtocolDeviationsSummaryGrid({
	summary,
}: ProtocolDeviationsSummaryGridProps) {
	return (
		<>
			<section className="grid gap-4 md:grid-cols-4">
				<SummaryCard title="Total" value={summary.totalDeviations} />
				<SummaryCard title="Open" value={summary.openDeviations} />
				<SummaryCard title="In Review" value={summary.inReviewDeviations} />
				<SummaryCard title="Resolved" value={summary.resolvedDeviations} />
			</section>

			<section className="grid gap-4 md:grid-cols-3">
				<SummaryCard title="Minor" value={summary.minorDeviations} />
				<SummaryCard title="Major" value={summary.majorDeviations} />
				<SummaryCard title="Critical" value={summary.criticalDeviations} />
			</section>
		</>
	);
}
