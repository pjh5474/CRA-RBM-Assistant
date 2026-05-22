import { RiskSite } from "@/types/risk";

interface RiskBadgeProps {
	level: RiskSite["riskLevel"];
}

const RISK_LEVEL_STYLES: Record<RiskSite["riskLevel"], string> = {
	High: "bg-red-50 text-red-700",
	Medium: "bg-amber-50 text-amber-700",
	Low: "bg-emerald-50 text-emerald-700",
};

export function RiskBadge({ level }: RiskBadgeProps) {
	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${RISK_LEVEL_STYLES[level]}`}
		>
			{level}
		</span>
	);
}
