import { DelegationTrainingChecksList } from "@/components/delegation-training/DelegationTrainingChecksList";
import { DelegationTrainingHeader } from "@/components/delegation-training/DelegationTrainingHeader";
import { DelegationTrainingReviewSummary } from "@/components/delegation-training/DelegationTrainingReviewSummary";
import { DelegationTrainingSummaryGrid } from "@/components/delegation-training/DelegationTrainingSummaryGrid";
import { SiteStudyNav } from "@/components/layout/SiteStudyNav";
import { PortfolioPrototypeNotice } from "@/components/ui/PortfolioPrototypeNotice";
import { ScenarioNote } from "@/components/ui/ScenarioNote";
import { DelegationTrainingCheck } from "@/types/delegationTraining";

interface DelegationTrainingViewProps {
	check: DelegationTrainingCheck;
}

export function DelegationTrainingView({ check }: DelegationTrainingViewProps) {
	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<SiteStudyNav studyId={check.studyId} siteId={check.siteId} />

				<DelegationTrainingHeader siteName={check.siteName} />

				<DelegationTrainingSummaryGrid check={check} />

				<DelegationTrainingReviewSummary check={check} />

				<ScenarioNote>
					This scenario-based synthetic dataset may include staff members whose
					protocol training or GCP training evidence is missing or completed
					after delegation start date. The purpose is to demonstrate how CRA
					review logic can identify delegation and training timing
					inconsistencies.
				</ScenarioNote>

				<DelegationTrainingChecksList checks={check.checks} />

				<PortfolioPrototypeNotice>
					This check uses scenario-based synthetic delegation and training
					records. It is designed to demonstrate CRA-oriented review logic and
					does not replace sponsor-approved delegation log review procedures.
				</PortfolioPrototypeNotice>
			</div>
		</main>
	);
}
