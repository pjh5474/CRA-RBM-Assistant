import { EssentialDocumentReadiness } from "@/types/essentialDocument";
import { IcfVersionCheck } from "@/types/icf";
import { MonitoringReportDraft } from "@/types/monitoringReport";
import { ProtocolDeviationSummary } from "@/types/protocolDeviation";
import { DelegationTrainingCheck } from "@/types/delegationTraining";
import { RiskSite } from "@/types/risk";

export interface SiteReviewStudySummary {
	studyId: string;
	title: string;
	phase: string;
	indication: string;
	sponsor: string;
}

export interface SiteReviewModule {
	title: string;
	description: string;
	href: string;
	statusLabel: string;
}

export interface SiteReviewSummary {
	study: SiteReviewStudySummary;
	site: RiskSite;
	essentialDocuments: EssentialDocumentReadiness;
	protocolDeviations: ProtocolDeviationSummary;
	icfVersionCheck: IcfVersionCheck;
	monitoringReportDraft: MonitoringReportDraft;
	delegationTrainingCheck: DelegationTrainingCheck;
	modules: SiteReviewModule[];
}
