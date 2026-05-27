import { ChecklistItem } from "@/types/checklist";
import { RiskSite } from "@/types/risk";
import { StudyDetail, StudySummary } from "@/types/study";
import { SiteActionItems } from "@/types/actionItem";
import {
	ClinicalTrialDetail,
	ClinicalTrialSearchResponse,
	ImportClinicalTrialResponse,
} from "@/types/clinicalTrial";
import { AuditLog } from "@/types/auditLog";
import { MonitoringReportDraft } from "@/types/monitoringReport";
import { EssentialDocumentReadiness } from "@/types/essentialDocument";
import { ProtocolDeviationSummary } from "@/types/protocolDeviation";
import { IcfVersionCheck } from "@/types/icf";
import { SiteReviewSummary } from "@/types/siteReview";
import { DelegationTrainingCheck } from "@/types/delegationTraining";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

async function fetchApi<T>(path: string, options?: RequestInit): Promise<T> {
	if (!API_BASE_URL) {
		throw new Error("NEXT_PUBLIC_API_BASE_URL is not defined");
	}

	const response = await fetch(`${API_BASE_URL}${path}`, {
		cache: "no-store",
		...options,
	});

	if (!response.ok) {
		throw new Error(
			`API request failed: ${response.status} ${response.statusText}`,
		);
	}

	return response.json();
}

export function getStudies(): Promise<StudySummary[]> {
	return fetchApi<StudySummary[]>("/api/studies");
}

export function getStudyDetail(studyId: string): Promise<StudyDetail> {
	return fetchApi<StudyDetail>(`/api/studies/${studyId}`);
}

export function getStudyRiskSites(studyId: string): Promise<RiskSite[]> {
	return fetchApi<RiskSite[]>(`/api/studies/${studyId}/risk-sites`);
}

export function getSivChecklist(): Promise<ChecklistItem[]> {
	return fetchApi<ChecklistItem[]>("/api/checklists/siv");
}

export function getImvChecklist(): Promise<ChecklistItem[]> {
	return fetchApi<ChecklistItem[]>("/api/checklists/imv");
}

export function getStudyActionItems(
	studyId: string,
): Promise<SiteActionItems[]> {
	return fetchApi<SiteActionItems[]>(`/api/studies/${studyId}/action-items`);
}

export function searchClinicalTrials(
	query: string,
	pageSize = 10,
): Promise<ClinicalTrialSearchResponse> {
	const searchParams = new URLSearchParams({
		query,
		page_size: String(pageSize),
	});

	return fetchApi<ClinicalTrialSearchResponse>(
		`/api/external/clinical-trials/search?${searchParams.toString()}`,
	);
}

export function getClinicalTrialDetail(
	nctId: string,
): Promise<ClinicalTrialDetail> {
	return fetchApi<ClinicalTrialDetail>(
		`/api/external/clinical-trials/${nctId}`,
	);
}

export function importClinicalTrialToSupabase(
	nctId: string,
	accessToken: string,
): Promise<ImportClinicalTrialResponse> {
	return fetchApi<ImportClinicalTrialResponse>(
		`/api/external/clinical-trials/${nctId}/import`,
		{
			method: "POST",
			headers: {
				Authorization: `Bearer ${accessToken}`,
			},
		},
	);
}

export function getAuditLogs(params?: {
	limit?: number;
	tableName?: string;
	action?: string;
}): Promise<AuditLog[]> {
	const searchParams = new URLSearchParams();

	if (params?.limit) {
		searchParams.set("limit", String(params.limit));
	}

	if (params?.tableName) {
		searchParams.set("table_name", params.tableName);
	}

	if (params?.action) {
		searchParams.set("action", params.action);
	}

	const queryString = searchParams.toString();

	return fetchApi<AuditLog[]>(
		`/api/audit-logs${queryString ? `?${queryString}` : ""}`,
	);
}

export function getMonitoringReportDraft(
	studyId: string,
	siteId: string,
): Promise<MonitoringReportDraft> {
	return fetchApi<MonitoringReportDraft>(
		`/api/studies/${studyId}/sites/${siteId}/monitoring-report-draft`,
	);
}

export function getEssentialDocumentReadiness(
	studyId: string,
	siteId: string,
): Promise<EssentialDocumentReadiness> {
	return fetchApi<EssentialDocumentReadiness>(
		`/api/studies/${studyId}/sites/${siteId}/essential-documents`,
	);
}

export function getProtocolDeviationSummary(
	studyId: string,
	siteId: string,
): Promise<ProtocolDeviationSummary> {
	return fetchApi<ProtocolDeviationSummary>(
		`/api/studies/${studyId}/sites/${siteId}/protocol-deviations`,
	);
}

export function getIcfVersionCheck(
	studyId: string,
	siteId: string,
): Promise<IcfVersionCheck> {
	return fetchApi<IcfVersionCheck>(
		`/api/studies/${studyId}/sites/${siteId}/icf-version-check`,
	);
}

export function getSiteReviewSummary(
	studyId: string,
	siteId: string,
): Promise<SiteReviewSummary> {
	return fetchApi<SiteReviewSummary>(
		`/api/studies/${studyId}/sites/${siteId}/review-summary`,
	);
}

export function getDelegationTrainingCheck(
	studyId: string,
	siteId: string,
): Promise<DelegationTrainingCheck> {
	return fetchApi<DelegationTrainingCheck>(
		`/api/studies/${studyId}/sites/${siteId}/delegation-training-check`,
	);
}
