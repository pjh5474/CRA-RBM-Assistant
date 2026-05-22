import { ChecklistItem } from "@/types/checklist";
import { RiskSite } from "@/types/risk";
import { StudyDetail, StudySummary } from "@/types/study";

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
