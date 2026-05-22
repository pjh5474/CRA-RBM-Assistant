import { PageContainer } from "@/components/layout/PageContainer";
import { StudyCard } from "@/components/study/StudyCard";
import { getStudies } from "@/lib/api";
import Link from "next/link";

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
				<div className="mt-5 flex gap-2">
					<Link
						href="/study-import"
						className="inline-flex rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-800"
					>
						Import Public Study
					</Link>
					<Link
						href="/audit-logs"
						className="inline-flex rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-800"
					>
						Audit Logs
					</Link>
				</div>
			</section>

			<section className="grid gap-4 md:grid-cols-2">
				{studies.map((study) => (
					<StudyCard key={study.studyId} study={study} />
				))}
			</section>
		</PageContainer>
	);
}
