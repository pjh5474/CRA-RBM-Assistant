"use client";

import { type SubmitEvent, useState } from "react";
import { SearchResultsPanel } from "@/components/study-import/SearchResultsPanel";
import { StudyImportHeader } from "@/components/study-import/StudyImportHeader";
import { StudyImportSearchForm } from "@/components/study-import/StudyImportSearchForm";
import { StudyPreviewPanel } from "@/components/study-import/StudyPreviewPanel";
import {
	getClinicalTrialDetail,
	importClinicalTrialToSupabase,
	searchClinicalTrials,
} from "@/lib/api";
import {
	ClinicalTrialDetail,
	ClinicalTrialSearchItem,
} from "@/types/clinicalTrial";

export function StudyImportView() {
	const [query, setQuery] = useState("diabetes");
	const [results, setResults] = useState<ClinicalTrialSearchItem[]>([]);
	const [selectedStudy, setSelectedStudy] =
		useState<ClinicalTrialDetail | null>(null);
	const [isSearching, setIsSearching] = useState(false);
	const [isLoadingDetail, setIsLoadingDetail] = useState(false);
	const [isImporting, setIsImporting] = useState(false);
	const [importedStudyId, setImportedStudyId] = useState<string | null>(null);
	const [importStatusMessage, setImportStatusMessage] = useState<string | null>(
		null,
	);
	const [importStatus, setImportStatus] = useState<
		"created" | "updated" | null
	>(null);
	const [demoDataCreated, setDemoDataCreated] = useState(false);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);

	async function handleSearch(event: SubmitEvent<HTMLFormElement>) {
		event.preventDefault();

		if (!query.trim()) {
			setErrorMessage("Please enter a search keyword.");
			return;
		}

		try {
			setIsSearching(true);
			setErrorMessage(null);
			setSelectedStudy(null);
			setImportedStudyId(null);
			setImportStatusMessage(null);
			setImportStatus(null);
			setDemoDataCreated(false);

			const response = await searchClinicalTrials(query.trim(), 10);
			setResults(response.results);
		} catch (error) {
			console.error(error);
			setErrorMessage("Failed to search ClinicalTrials.gov data.");
		} finally {
			setIsSearching(false);
		}
	}

	async function handleSelectStudy(nctId: string) {
		try {
			setIsLoadingDetail(true);
			setErrorMessage(null);
			setImportedStudyId(null);
			setImportStatusMessage(null);
			setImportStatus(null);
			setDemoDataCreated(false);

			const detail = await getClinicalTrialDetail(nctId);
			setSelectedStudy(detail);
		} catch (error) {
			console.error(error);
			setErrorMessage(`Failed to load detail for ${nctId}.`);
		} finally {
			setIsLoadingDetail(false);
		}
	}

	async function handleImportStudy() {
		if (!selectedStudy) {
			setErrorMessage("Please select a study before importing.");
			return;
		}

		try {
			setIsImporting(true);
			setErrorMessage(null);
			setImportStatusMessage(null);
			setImportStatus(null);
			setDemoDataCreated(false);

			const response = await importClinicalTrialToSupabase(selectedStudy.nctId);

			setImportedStudyId(response.study.studyId);
			setImportStatus(response.status);
			setImportStatusMessage(response.message);
			setDemoDataCreated(response.demoDataCreated);
		} catch (error) {
			console.error(error);
			setErrorMessage(`Failed to import ${selectedStudy.nctId} into Supabase.`);
		} finally {
			setIsImporting(false);
		}
	}

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-7xl space-y-8">
				<StudyImportHeader />

				<StudyImportSearchForm
					query={query}
					isSearching={isSearching}
					errorMessage={errorMessage}
					onQueryChange={setQuery}
					onSubmit={handleSearch}
				/>

				<section className="grid gap-6 lg:grid-cols-2">
					<SearchResultsPanel
						results={results}
						selectedNctId={selectedStudy?.nctId}
						isLoadingDetail={isLoadingDetail}
						onSelectStudy={handleSelectStudy}
					/>

					<StudyPreviewPanel
						selectedStudy={selectedStudy}
						isLoadingDetail={isLoadingDetail}
						isImporting={isImporting}
						importedStudyId={importedStudyId}
						importStatus={importStatus}
						importStatusMessage={importStatusMessage}
						demoDataCreated={demoDataCreated}
						onImportStudy={handleImportStudy}
					/>
				</section>
			</div>
		</main>
	);
}
