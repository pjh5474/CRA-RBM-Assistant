import Link from "next/link";
import { PhaseBadge } from "@/components/ui/PhaseBadge";
import { StudySummary } from "@/types/study";

interface StudyCardProps {
	study: StudySummary;
}

export function StudyCard({ study }: StudyCardProps) {
	return (
		<Link
			href={`/studies/${study.studyId}`}
			className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-md"
		>
			<div className="mb-3 flex items-center justify-between">
				<PhaseBadge phase={study.phase} />
				<span className="text-xs text-slate-500">{study.studyId}</span>
			</div>

			<h2 className="line-clamp-3 text-lg font-semibold text-slate-900">
				{study.title}
			</h2>

			<div className="mt-4 space-y-1 text-sm text-slate-600">
				<p>
					<span className="font-medium text-slate-800">Indication:</span>{" "}
					{study.indication}
				</p>
				<p>
					<span className="font-medium text-slate-800">Sponsor:</span>{" "}
					{study.sponsor}
				</p>
			</div>
		</Link>
	);
}
