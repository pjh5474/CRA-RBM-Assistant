import { MonitoringReportView } from "@/components/monitoring-report/MonitoringReportView";
import { getMonitoringReportDraft } from "@/lib/api";

interface MonitoringReportPageProps {
	params: Promise<{
		studyId: string;
		siteId: string;
	}>;
}

export default async function MonitoringReportPage({
	params,
}: MonitoringReportPageProps) {
	const { studyId, siteId } = await params;
	const report = await getMonitoringReportDraft(studyId, siteId);

	return <MonitoringReportView report={report} />;
}
