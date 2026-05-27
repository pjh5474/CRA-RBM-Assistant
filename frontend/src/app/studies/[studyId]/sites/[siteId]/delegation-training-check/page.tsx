import { DelegationTrainingView } from "@/components/delegation-training/DelegationTrainingView";
import { getDelegationTrainingCheck } from "@/lib/api";

interface DelegationTrainingCheckPageProps {
	params: Promise<{
		studyId: string;
		siteId: string;
	}>;
}

export default async function DelegationTrainingCheckPage({
	params,
}: DelegationTrainingCheckPageProps) {
	const { studyId, siteId } = await params;
	const check = await getDelegationTrainingCheck(studyId, siteId);

	return <DelegationTrainingView check={check} />;
}
