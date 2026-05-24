import { DocumentStatusSummary } from "@/components/essential-documents/DocumentStatusSummary";
import { EssentialDocumentsHeader } from "@/components/essential-documents/EssentialDocumentsHeader";
import { EssentialDocumentsSummaryGrid } from "@/components/essential-documents/EssentialDocumentsSummaryGrid";
import { EssentialDocumentsTable } from "@/components/essential-documents/EssentialDocumentsTable";
import { ReadinessBar } from "@/components/essential-documents/ReadinessBar";
import { SiteStudyNav } from "@/components/layout/SiteStudyNav";
import { PortfolioPrototypeNotice } from "@/components/ui/PortfolioPrototypeNotice";
import { EssentialDocumentReadiness } from "@/types/essentialDocument";

interface EssentialDocumentsViewProps {
	readiness: EssentialDocumentReadiness;
}

export function EssentialDocumentsView({
	readiness,
}: EssentialDocumentsViewProps) {
	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<SiteStudyNav studyId={readiness.studyId} siteId={readiness.siteId} />

				<EssentialDocumentsHeader siteName={readiness.siteName} />

				<EssentialDocumentsSummaryGrid readiness={readiness} />

				<ReadinessBar readinessScore={readiness.readinessScore} />

				<DocumentStatusSummary readiness={readiness} />

				<EssentialDocumentsTable documents={readiness.documents} />

				<PortfolioPrototypeNotice>
					This tracker uses synthetic document data and simplified readiness
					scoring. It is designed to demonstrate CRA-oriented document readiness
					review and does not replace sponsor-approved TMF/ISF systems or CRA
					judgment.
				</PortfolioPrototypeNotice>
			</div>
		</main>
	);
}
