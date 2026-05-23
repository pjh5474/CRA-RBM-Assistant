import Link from "next/link";

interface SiteStudyNavProps {
	studyId: string;
}

export function SiteStudyNav({ studyId }: SiteStudyNavProps) {
	return (
		<div className="flex flex-wrap gap-4">
			<Link
				href={`/studies/${studyId}/risk-dashboard`}
				className="text-sm font-medium text-blue-700 hover:text-blue-800"
			>
				← Back to risk dashboard
			</Link>

			<Link
				href={`/studies/${studyId}`}
				className="text-sm font-medium text-blue-700 hover:text-blue-800"
			>
				Back to study overview
			</Link>
		</div>
	);
}
