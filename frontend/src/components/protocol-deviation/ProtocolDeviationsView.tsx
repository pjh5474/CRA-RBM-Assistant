import { DeviationReviewSummary } from "@/components/protocol-deviation/DeviationReviewSummary";
import { ProtocolDeviationsHeader } from "@/components/protocol-deviation/ProtocolDeviationsHeader";
import { ProtocolDeviationsList } from "@/components/protocol-deviation/ProtocolDeviationsList";
import { ProtocolDeviationsSummaryGrid } from "@/components/protocol-deviation/ProtocolDeviationsSummaryGrid";
import { SiteStudyNav } from "@/components/layout/SiteStudyNav";
import { PortfolioPrototypeNotice } from "@/components/ui/PortfolioPrototypeNotice";
import { ScenarioNote } from "@/components/ui/ScenarioNote";
import { ProtocolDeviationSummary } from "@/types/protocolDeviation";

interface ProtocolDeviationsViewProps {
	summary: ProtocolDeviationSummary;
}

export function ProtocolDeviationsView({
	summary,
}: ProtocolDeviationsViewProps) {
	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<SiteStudyNav studyId={summary.studyId} siteId={summary.siteId} />

				<ProtocolDeviationsHeader siteName={summary.siteName} />

				<ScenarioNote>
					This dataset includes a visit window deviation, missing assessment,
					and SAE reporting delay to demonstrate how protocol compliance
					findings can be structured by severity, status, root cause, and
					corrective/preventive action.
				</ScenarioNote>

				<ProtocolDeviationsSummaryGrid summary={summary} />

				<DeviationReviewSummary summary={summary} />

				<ProtocolDeviationsList deviations={summary.deviations} />

				<PortfolioPrototypeNotice>
					This tracker uses synthetic protocol deviation data and simplified
					categorization. It is designed to demonstrate CRA-oriented issue
					tracking and does not replace sponsor-approved deviation management
					processes or CRA judgment.
				</PortfolioPrototypeNotice>
			</div>
		</main>
	);
}
