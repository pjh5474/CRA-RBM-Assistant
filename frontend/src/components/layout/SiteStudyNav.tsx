import Link from "next/link";

interface SiteStudyNavProps {
	studyId: string;
	siteId: string;
}

export function SiteStudyNav({ studyId, siteId }: SiteStudyNavProps) {
	return (
		<div className="flex flex-wrap gap-4">
			<Link
				href={`/studies/${studyId}/sites/${siteId}`}
				className="text-sm font-medium text-blue-700 hover:text-blue-800"
			>
				← Back to site review
			</Link>

			<Link
				href={`/studies/${studyId}/risk-dashboard`}
				className="text-sm font-medium text-blue-700 hover:text-blue-800"
			>
				Back to risk dashboard
			</Link>
		</div>
	);
}
