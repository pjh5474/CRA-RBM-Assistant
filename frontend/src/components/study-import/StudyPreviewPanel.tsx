import Link from "next/link";
import { ListSection } from "@/components/study-import/ListSection";
import { PreviewGrid } from "@/components/study-import/PreviewGrid";
import { TextSection } from "@/components/study-import/TextSection";
import { ClinicalTrialDetail } from "@/types/clinicalTrial";

interface StudyPreviewPanelProps {
	selectedStudy: ClinicalTrialDetail | null;
	isLoadingDetail: boolean;
	isImporting: boolean;
	importedStudyId: string | null;
	importStatus: "created" | "updated" | null;
	importStatusMessage: string | null;
	demoDataCreated: boolean;
	isAuthenticated: boolean;
	onImportStudy: () => void;
}

export function StudyPreviewPanel({
	selectedStudy,
	isLoadingDetail,
	isImporting,
	importedStudyId,
	importStatus,
	importStatusMessage,
	demoDataCreated,
	isAuthenticated,
	onImportStudy,
}: StudyPreviewPanelProps) {
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

						<div className="space-y-3">
							{importStatusMessage && (
								<div
									className={`rounded-xl border px-4 py-3 text-sm ${
										importStatus === "created"
											? "border-emerald-200 bg-emerald-50 text-emerald-700"
											: "border-blue-200 bg-blue-50 text-blue-700"
									}`}
								>
									<p className="font-semibold">
										{importStatus === "created" ? "Created" : "Updated"}
									</p>
									<p className="mt-1">{importStatusMessage}</p>

									{demoDataCreated && (
										<p className="mt-2 text-xs">
											Synthetic demo sites and monitoring metrics are available
											for the risk dashboard.
										</p>
									)}
								</div>
							)}
							<div className="flex flex-wrap gap-3">
								<button
									type="button"
									onClick={onImportStudy}
									disabled={isImporting || !isAuthenticated}
									className="rounded-xl bg-blue-700 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-800 disabled:cursor-not-allowed disabled:bg-slate-400"
								>
									{isImporting ? "Importing..." : "Import to Supabase"}
								</button>

								{!isAuthenticated && (
									<Link
										href="/login"
										className="rounded-xl border border-slate-300 bg-white px-4 py-2 text-sm font-semibold text-slate-700 hover:bg-slate-50"
									>
										Sign in to import
									</Link>
								)}

								{!isAuthenticated && (
									<p className="rounded-xl bg-amber-50 px-4 py-3 text-sm text-amber-700">
										Sign in is required to import studies and create demo
										operational data. Public search and preview are available
										without sign-in.
									</p>
								)}

								{importedStudyId && (
									<>
										<Link
											href={`/studies/${importedStudyId}`}
											className="rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-800"
										>
											View Imported Study
										</Link>

										<Link
											href={`/studies/${importedStudyId}/risk-dashboard`}
											className="rounded-xl bg-emerald-700 px-4 py-2 text-sm font-semibold text-white hover:bg-emerald-800"
										>
											View Risk Dashboard
										</Link>
									</>
								)}
							</div>
						</div>
					</div>
				)}
			</div>
		</section>
	);
}
