import { FormEvent } from "react";

interface StudyImportSearchFormProps {
	query: string;
	isSearching: boolean;
	errorMessage: string | null;
	onQueryChange: (value: string) => void;
	onSubmit: (event: FormEvent<HTMLFormElement>) => void;
}

export function StudyImportSearchForm({
	query,
	isSearching,
	errorMessage,
	onQueryChange,
	onSubmit,
}: StudyImportSearchFormProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<form
				onSubmit={onSubmit}
				className="flex flex-col gap-3 md:flex-row"
			>
				<input
					value={query}
					onChange={(event) => onQueryChange(event.target.value)}
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
	);
}
