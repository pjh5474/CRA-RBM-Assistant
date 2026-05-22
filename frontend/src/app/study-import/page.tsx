"use client";

import Link from "next/link";
import { FormEvent, useState } from "react";
import { getClinicalTrialDetail, searchClinicalTrials } from "@/lib/api";
import {
	ClinicalTrialDetail,
	ClinicalTrialSearchItem,
} from "@/types/clinicalTrial";

export default function StudyImportPage() {
	const [query, setQuery] = useState("diabetes");
	const [results, setResults] = useState<ClinicalTrialSearchItem[]>([]);
	const [selectedStudy, setSelectedStudy] =
		useState<ClinicalTrialDetail | null>(null);
	const [isSearching, setIsSearching] = useState(false);
	const [isLoadingDetail, setIsLoadingDetail] = useState(false);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);

	async function handleSearch(event: FormEvent<HTMLFormElement>) {
		event.preventDefault();

		if (!query.trim()) {
			setErrorMessage("Please enter a search keyword.");
			return;
		}

		try {
			setIsSearching(true);
			setErrorMessage(null);
			setSelectedStudy(null);

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

			const detail = await getClinicalTrialDetail(nctId);
			setSelectedStudy(detail);
		} catch (error) {
			console.error(error);
			setErrorMessage(`Failed to load detail for ${nctId}.`);
		} finally {
			setIsLoadingDetail(false);
		}
	}

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-7xl space-y-8">
				<div>
					<Link href="/" className="text-sm font-medium text-blue-700">
						← Back to study list
					</Link>
				</div>

				<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
					<p className="mb-2 text-sm font-semibold text-blue-700">
						ClinicalTrials.gov Study Search
					</p>
					<h1 className="text-2xl font-bold text-slate-900">
						Import Public Study Preview
					</h1>
					<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
						Search public clinical trial registry data and preview structured
						study information. This page currently supports search and preview
						only. Importing selected studies into Supabase can be added in the
						next step.
					</p>
				</section>

				<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
					<form
						onSubmit={handleSearch}
						className="flex flex-col gap-3 md:flex-row"
					>
						<input
							value={query}
							onChange={(event) => setQuery(event.target.value)}
							placeholder="Search condition, disease, intervention..."
							className="min-h-11 flex-1 rounded-xl border border-slate-300 px-4 text-sm outline-none focus:border-blue-600 focus:ring-2 focus:ring-blue-100"
						/>
						<button
							type="submit"
							disabled={isSearching}
							className="rounded-xl bg-blue-700 px-5 py-2.5 text-sm font-semibold text-white hover:bg-blue-800 disabled:cursor-not-allowed disabled:bg-slate-400"
						>
							{isSearching ? "Searching..." : "Search"}
						</button>
					</form>

					{errorMessage && (
						<p className="mt-4 rounded-xl bg-red-50 px-4 py-3 text-sm text-red-700">
							{errorMessage}
						</p>
					)}
				</section>

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
					/>
				</section>
			</div>
		</main>
	);
}

function SearchResultsPanel({
	results,
	selectedNctId,
	isLoadingDetail,
	onSelectStudy,
}: {
	results: ClinicalTrialSearchItem[];
	selectedNctId?: string;
	isLoadingDetail: boolean;
	onSelectStudy: (nctId: string) => void;
}) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white shadow-sm">
			<div className="border-b border-slate-200 p-5">
				<h2 className="text-lg font-bold text-slate-900">Search Results</h2>
				<p className="mt-1 text-sm text-slate-600">
					Select an NCT ID to preview study details.
				</p>
			</div>

			<div className="max-h-[720px] overflow-y-auto p-5">
				{results.length === 0 ? (
					<p className="rounded-xl border border-dashed border-slate-300 p-8 text-center text-sm text-slate-500">
						No search results yet.
					</p>
				) : (
					<div className="space-y-4">
						{results.map((study) => {
							const isSelected = selectedNctId === study.nctId;

							return (
								<button
									key={study.nctId}
									type="button"
									disabled={isLoadingDetail}
									onClick={() => onSelectStudy(study.nctId)}
									className={`w-full rounded-xl border p-4 text-left transition hover:border-blue-300 hover:bg-blue-50 ${
										isSelected
											? "border-blue-500 bg-blue-50"
											: "border-slate-200 bg-white"
									}`}
								>
									<div className="mb-2 flex flex-wrap items-center gap-2">
										<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
											{study.nctId}
										</span>
										{study.status && (
											<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
												{study.status}
											</span>
										)}
									</div>

									<h3 className="text-sm font-semibold leading-6 text-slate-900">
										{study.title}
									</h3>

									<MetadataRow label="Phase" values={study.phases} />
									<MetadataRow label="Condition" values={study.conditions} />
									<MetadataRow
										label="Intervention"
										values={study.interventions}
									/>
								</button>
							);
						})}
					</div>
				)}
			</div>
		</section>
	);
}

function StudyPreviewPanel({
	selectedStudy,
	isLoadingDetail,
}: {
	selectedStudy: ClinicalTrialDetail | null;
	isLoadingDetail: boolean;
}) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white shadow-sm">
			<div className="border-b border-slate-200 p-5">
				<h2 className="text-lg font-bold text-slate-900">
					Study Detail Preview
				</h2>
				<p className="mt-1 text-sm text-slate-600">
					Key registry information mapped for CRA-oriented review.
				</p>
			</div>

			<div className="max-h-[720px] overflow-y-auto p-5">
				{isLoadingDetail ? (
					<p className="rounded-xl bg-slate-50 p-6 text-sm text-slate-600">
						Loading study detail...
					</p>
				) : !selectedStudy ? (
					<p className="rounded-xl border border-dashed border-slate-300 p-8 text-center text-sm text-slate-500">
						Select a study from the search results.
					</p>
				) : (
					<div className="space-y-6">
						<div>
							<div className="mb-3 flex flex-wrap items-center gap-2">
								<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
									{selectedStudy.nctId}
								</span>
								{selectedStudy.status && (
									<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
										{selectedStudy.status}
									</span>
								)}
							</div>

							<h3 className="text-xl font-bold leading-7 text-slate-900">
								{selectedStudy.title}
							</h3>
						</div>

						<PreviewGrid study={selectedStudy} />

						{selectedStudy.briefSummary && (
							<TextSection
								title="Brief Summary"
								content={selectedStudy.briefSummary}
							/>
						)}

						<ListSection
							title="Primary Outcomes"
							items={selectedStudy.primaryOutcomes}
						/>

						<ListSection
							title="Secondary Outcomes"
							items={selectedStudy.secondaryOutcomes}
						/>

						{selectedStudy.eligibilityCriteria && (
							<TextSection
								title="Eligibility Criteria"
								content={selectedStudy.eligibilityCriteria}
							/>
						)}
					</div>
				)}
			</div>
		</section>
	);
}

function PreviewGrid({ study }: { study: ClinicalTrialDetail }) {
	const rows = [
		{ label: "Study Type", value: study.studyType },
		{ label: "Allocation", value: study.allocation },
		{ label: "Masking", value: study.masking },
		{ label: "Who Masked", value: study.whoMasked.join(", ") },
		{ label: "Phase", value: study.phases.join(", ") },
		{ label: "Conditions", value: study.conditions.join(", ") },
		{ label: "Interventions", value: study.interventions.join(", ") },
	];

	return (
		<div className="grid gap-3 md:grid-cols-2">
			{rows.map((row) => (
				<div
					key={row.label}
					className="rounded-xl border border-slate-200 bg-slate-50 p-4"
				>
					<p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
						{row.label}
					</p>
					<p className="mt-2 text-sm text-slate-900">
						{row.value || "Not available"}
					</p>
				</div>
			))}
		</div>
	);
}

function MetadataRow({ label, values }: { label: string; values: string[] }) {
	if (values.length === 0) {
		return null;
	}

	return (
		<p className="mt-2 text-xs text-slate-600">
			<span className="font-semibold text-slate-800">{label}: </span>
			{values.slice(0, 3).join(", ")}
			{values.length > 3 ? "..." : ""}
		</p>
	);
}

function TextSection({ title, content }: { title: string; content: string }) {
	return (
		<section>
			<h4 className="mb-2 text-sm font-bold text-slate-900">{title}</h4>
			<p className="whitespace-pre-line rounded-xl bg-slate-50 p-4 text-sm leading-6 text-slate-700">
				{content}
			</p>
		</section>
	);
}

function ListSection({ title, items }: { title: string; items: string[] }) {
	return (
		<section>
			<h4 className="mb-2 text-sm font-bold text-slate-900">{title}</h4>
			{items.length === 0 ? (
				<p className="rounded-xl bg-slate-50 p-4 text-sm text-slate-500">
					Not available
				</p>
			) : (
				<ul className="space-y-2 rounded-xl bg-slate-50 p-4">
					{items.map((item, index) => (
						<li
							key={`${title}-${index}`}
							className="text-sm leading-6 text-slate-700"
						>
							- {item}
						</li>
					))}
				</ul>
			)}
		</section>
	);
}
