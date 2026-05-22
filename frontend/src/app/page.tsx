import { PageContainer } from "@/components/layout/PageContainer";
import { StudyCard } from "@/components/study/StudyCard";
import { getStudies } from "@/lib/api";

export default async function HomePage() {
	const studies = await getStudies();

	return (
		<PageContainer>
			<section className="mb-8">
				<p className="mb-2 text-sm font-semibold text-blue-700">
					CRA-RBM Assistant
				</p>
				<h1 className="text-3xl font-bold text-slate-900">
					Clinical Study Monitoring Dashboard
				</h1>
				<p className="mt-3 max-w-3xl text-slate-600">
					Select a sample study to review structured protocol information, CRA
					checklist items, and site-level risk indicators.
				</p>
			</section>

			<section className="grid gap-4 md:grid-cols-2">
				{studies.map((study) => (
					<StudyCard key={study.studyId} study={study} />
				))}
			</section>
		</PageContainer>
	);
}
