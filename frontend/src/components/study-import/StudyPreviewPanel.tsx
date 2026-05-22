import { ListSection } from "@/components/study-import/ListSection";
import { PreviewGrid } from "@/components/study-import/PreviewGrid";
import { TextSection } from "@/components/study-import/TextSection";
import { ClinicalTrialDetail } from "@/types/clinicalTrial";

interface StudyPreviewPanelProps {
	selectedStudy: ClinicalTrialDetail | null;
	isLoadingDetail: boolean;
}

export function StudyPreviewPanel({
	selectedStudy,
	isLoadingDetail,
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
					</div>
				)}
			</div>
		</section>
	);
}
