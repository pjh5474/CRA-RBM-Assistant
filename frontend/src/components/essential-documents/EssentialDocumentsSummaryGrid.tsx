import { SummaryCard } from "@/components/ui/SummaryCard";
import { EssentialDocumentReadiness } from "@/types/essentialDocument";

interface EssentialDocumentsSummaryGridProps {
	readiness: EssentialDocumentReadiness;
}

export function EssentialDocumentsSummaryGrid({
	readiness,
}: EssentialDocumentsSummaryGridProps) {
	return (
		<section className="grid gap-4 md:grid-cols-5">
			<SummaryCard
				title="Readiness Score"
				value={`${readiness.readinessScore}%`}
				emphasis
			/>
			<SummaryCard title="Total" value={readiness.totalDocuments} />
			<SummaryCard title="Ready" value={readiness.readyDocuments} />
			<SummaryCard title="Missing" value={readiness.missingDocuments} />
			<SummaryCard title="Expired" value={readiness.expiredDocuments} />
		</section>
	);
}
