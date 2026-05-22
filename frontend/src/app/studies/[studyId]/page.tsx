import Link from "next/link";
import { ChecklistPanel } from "@/components/checklist/ChecklistPanel";
import { BackLink } from "@/components/layout/BackLink";
import { PageContainer } from "@/components/layout/PageContainer";
import { InfoCard } from "@/components/ui/InfoCard";
import { PhaseBadge } from "@/components/ui/PhaseBadge";
import { getImvChecklist, getSivChecklist, getStudyDetail } from "@/lib/api";

interface StudyDetailPageProps {
	params: Promise<{
		studyId: string;
	}>;
}

export default async function StudyDetailPage({
	params,
}: StudyDetailPageProps) {
	const { studyId } = await params;

	const [study, sivChecklist, imvChecklist] = await Promise.all([
		getStudyDetail(studyId),
		getSivChecklist(),
		getImvChecklist(),
	]);

	return (
		<PageContainer className="space-y-8">
			<div>
				<BackLink href="/">← Back to study list</BackLink>
			</div>

			<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
				<div className="mb-4 flex flex-wrap items-center gap-2">
					<PhaseBadge phase={study.phase} />
					<span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-700">
						{study.indication}
					</span>
				</div>

				<h1 className="text-2xl font-bold text-slate-900">{study.title}</h1>

				<div className="mt-6 grid gap-4 md:grid-cols-2">
					<InfoCard title="Sponsor" value={study.sponsor} />
					<InfoCard title="Study ID" value={study.studyId} />
					<InfoCard
						title="Primary Endpoint"
						value={String(study.endpoints.primaryEndpoint)}
					/>
					<InfoCard
						title="Investigational Product"
						value={String(study.intervention.investigationalProduct)}
					/>
				</div>

				<div className="mt-6 flex flex-wrap gap-3">
					<Link
						href={`/studies/${study.studyId}/risk-dashboard`}
						className="inline-flex rounded-xl bg-blue-700 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-800"
					>
						View Site Risk Dashboard
					</Link>
					<Link
						href={`/studies/${study.studyId}/action-items`}
						className="inline-flex rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-800"
					>
						View CRA Action Items
					</Link>
				</div>
			</section>

			<section className="grid gap-6 lg:grid-cols-2">
				<ChecklistPanel title="SIV Checklist" items={sivChecklist} />
				<ChecklistPanel title="IMV Checklist" items={imvChecklist} />
			</section>
		</PageContainer>
	);
}
