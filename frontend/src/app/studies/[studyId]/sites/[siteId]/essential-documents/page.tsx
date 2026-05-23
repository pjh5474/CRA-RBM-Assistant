import { EssentialDocumentsView } from "@/components/essential-documents/EssentialDocumentsView";
import { getEssentialDocumentReadiness } from "@/lib/api";

interface EssentialDocumentsPageProps {
	params: Promise<{
		studyId: string;
		siteId: string;
	}>;
}

export default async function EssentialDocumentsPage({
	params,
}: EssentialDocumentsPageProps) {
	const { studyId, siteId } = await params;
	const readiness = await getEssentialDocumentReadiness(studyId, siteId);

	return <EssentialDocumentsView readiness={readiness} />;
}
