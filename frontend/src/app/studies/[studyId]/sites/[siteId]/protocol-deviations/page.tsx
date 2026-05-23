import { ProtocolDeviationsView } from "@/components/protocol-deviation/ProtocolDeviationsView";
import { getProtocolDeviationSummary } from "@/lib/api";

interface ProtocolDeviationPageProps {
	params: Promise<{
		studyId: string;
		siteId: string;
	}>;
}

export default async function ProtocolDeviationPage({
	params,
}: ProtocolDeviationPageProps) {
	const { studyId, siteId } = await params;
	const summary = await getProtocolDeviationSummary(studyId, siteId);

	return <ProtocolDeviationsView summary={summary} />;
}
