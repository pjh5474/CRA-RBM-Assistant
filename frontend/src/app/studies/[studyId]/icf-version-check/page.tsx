import Link from "next/link";
import { getIcfVersionCheck } from "@/lib/api";
import { IcfVersion, IcfVersionCheck, IcfVersionCheckItem } from "@/types/icf";

interface IcfVersionCheckPageProps {
	params: Promise<{
		studyId: string;
		siteId: string;
	}>;
}

export default async function IcfVersionCheckPage({
	params,
}: IcfVersionCheckPageProps) {
	const { studyId, siteId } = await params;
	const check = await getIcfVersionCheck(studyId, siteId);

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-6xl space-y-8">
				<div className="flex flex-wrap gap-4">
					<Link
						href={`/studies/${check.studyId}/risk-dashboard`}
						className="text-sm font-medium text-blue-700 hover:text-blue-800"
					>
						← Back to risk dashboard
					</Link>

					<Link
						href={`/studies/${check.studyId}`}
						className="text-sm font-medium text-blue-700 hover:text-blue-800"
					>
						Back to study overview
					</Link>
				</div>

				<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
					<p className="mb-2 text-sm font-semibold text-blue-700">
						ICF Version Control Check
					</p>

					<h1 className="text-2xl font-bold text-slate-900">
						{check.siteName}
					</h1>

					<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
						This page checks whether subject consent records are consistent with
						the ICF version that was effective on the consent date. It
						demonstrates date-based version control review for CRA monitoring.
					</p>
				</section>

				<section className="grid gap-4 md:grid-cols-3">
					<SummaryCard title="Total Consents" value={check.totalConsents} />
					<SummaryCard title="Valid Consents" value={check.validConsents} />
					<SummaryCard title="Issue Consents" value={check.issueConsents} />
				</section>

				<IcfReviewSummary check={check} />

				<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
					<h2 className="mb-4 text-lg font-bold text-slate-900">
						ICF Version History
					</h2>

					<div className="grid gap-4 md:grid-cols-2">
						{check.icfVersions.map((version) => (
							<IcfVersionCard key={version.icfVersionId} version={version} />
						))}
					</div>
				</section>

				<section className="space-y-5">
					<h2 className="text-lg font-bold text-slate-900">
						Subject Consent Checks
					</h2>

					{check.checks.length === 0 ? (
						<div className="rounded-2xl border border-dashed border-slate-300 bg-white p-10 text-center">
							<h3 className="text-lg font-semibold text-slate-900">
								No consent records
							</h3>
							<p className="mt-2 text-sm text-slate-600">
								No subject consent records were found for this site.
							</p>
						</div>
					) : (
						check.checks.map((item) => (
							<ConsentCheckCard key={item.consentId} item={item} />
						))
					)}
				</section>

				<section className="rounded-2xl border border-amber-200 bg-amber-50 p-5">
					<h2 className="text-sm font-bold text-amber-900">
						Portfolio Prototype Notice
					</h2>
					<p className="mt-2 text-sm leading-6 text-amber-800">
						This check uses synthetic consent data and simplified date-based
						logic. It is designed to demonstrate CRA-oriented ICF version review
						and does not replace sponsor-approved informed consent review
						procedures or CRA judgment.
					</p>
				</section>
			</div>
		</main>
	);
}

function SummaryCard({ title, value }: { title: string; value: number }) {
	return (
		<div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
			<p className="text-sm font-medium text-slate-500">{title}</p>
			<p className="mt-2 text-2xl font-bold text-slate-900">{value}</p>
		</div>
	);
}

function IcfReviewSummary({ check }: { check: IcfVersionCheck }) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<h2 className="text-lg font-bold text-slate-900">CRA Review Summary</h2>

			{check.issueConsents === 0 ? (
				<p className="mt-3 text-sm leading-6 text-slate-700">
					All subject consent records are consistent with the expected ICF
					version based on the consent date.
				</p>
			) : (
				<div className="mt-3 space-y-2 text-sm leading-6 text-slate-700">
					<p>
						This site has {check.issueConsents} consent version issue(s)
						requiring CRA review.
					</p>
					<ul className="space-y-1">
						<li>
							- Confirm whether the subject signed the correct IRB-approved ICF
							version.
						</li>
						<li>- Review source documentation and consent process notes.</li>
						<li>
							- Determine whether site retraining or documentation correction is
							required.
						</li>
					</ul>
				</div>
			)}
		</section>
	);
}

function IcfVersionCard({ version }: { version: IcfVersion }) {
	return (
		<article className="rounded-xl border border-slate-200 bg-slate-50 p-5">
			<div className="mb-3 flex flex-wrap items-center gap-2">
				<span className="rounded-full bg-slate-900 px-3 py-1 text-xs font-semibold text-white">
					Version {version.version}
				</span>
				<IcfStatusBadge status={version.status} />
			</div>

			<div className="space-y-2 text-sm text-slate-700">
				<p>
					<span className="font-semibold text-slate-900">
						IRB Approval Date:
					</span>{" "}
					{version.irbApprovalDate}
				</p>
				<p>
					<span className="font-semibold text-slate-900">Effective Date:</span>{" "}
					{version.effectiveDate}
				</p>
			</div>
		</article>
	);
}

function ConsentCheckCard({ item }: { item: IcfVersionCheckItem }) {
	return (
		<article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<div className="mb-5 flex flex-wrap items-start justify-between gap-4">
				<div>
					<div className="mb-2 flex flex-wrap gap-2">
						<ConsentStatusBadge status={item.status} />
						{item.issueType && (
							<span className="rounded-full bg-red-50 px-3 py-1 text-xs font-semibold text-red-700">
								{item.issueType}
							</span>
						)}
					</div>

					<h2 className="text-lg font-bold text-slate-900">
						{item.subjectCode}
					</h2>

					<p className="mt-2 text-sm text-slate-500">{item.consentId}</p>
				</div>
			</div>

			<div className="grid gap-4 md:grid-cols-2">
				<InfoBlock title="Signed ICF Version" value={item.signedIcfVersion} />
				<InfoBlock
					title="Expected ICF Version"
					value={item.expectedIcfVersion ?? "N/A"}
				/>
				<InfoBlock title="Consent Date" value={item.consentDate} />
				<InfoBlock title="Review Message" value={item.message} />
			</div>
		</article>
	);
}

function InfoBlock({ title, value }: { title: string; value: string }) {
	return (
		<div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
			<p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
				{title}
			</p>
			<p className="mt-2 text-sm leading-6 text-slate-800">{value}</p>
		</div>
	);
}

function IcfStatusBadge({ status }: { status: IcfVersion["status"] }) {
	const className =
		status === "Active"
			? "bg-emerald-50 text-emerald-700"
			: "bg-slate-100 text-slate-700";

	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${className}`}
		>
			{status}
		</span>
	);
}

function ConsentStatusBadge({
	status,
}: {
	status: IcfVersionCheckItem["status"];
}) {
	const className =
		status === "Valid"
			? "bg-emerald-50 text-emerald-700"
			: "bg-red-50 text-red-700";

	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${className}`}
		>
			{status}
		</span>
	);
}
