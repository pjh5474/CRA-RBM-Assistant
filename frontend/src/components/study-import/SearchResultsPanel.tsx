import { MetadataRow } from "@/components/study-import/MetadataRow";
import { ClinicalTrialSearchItem } from "@/types/clinicalTrial";

interface SearchResultsPanelProps {
	results: ClinicalTrialSearchItem[];
	selectedNctId?: string;
	isLoadingDetail: boolean;
	onSelectStudy: (nctId: string) => void;
}

export function SearchResultsPanel({
	results,
	selectedNctId,
	isLoadingDetail,
	onSelectStudy,
}: SearchResultsPanelProps) {
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
