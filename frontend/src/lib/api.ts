import { ChecklistItem } from "@/types/checklist";
import { RiskSite } from "@/types/risk";
import { StudyDetail, StudySummary } from "@/types/study";
import { SiteActionItems } from "@/types/actionItem";
import {
	ClinicalTrialDetail,
	ClinicalTrialSearchResponse,
} from "@/types/clinicalTrial";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

async function fetchApi<T>(path: string): Promise<T> {
	if (!API_BASE_URL) {
		throw new Error("NEXT_PUBLIC_API_BASE_URL is not defined");
	}

	const response = await fetch(`${API_BASE_URL}${path}`, {
		cache: "no-store",
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
