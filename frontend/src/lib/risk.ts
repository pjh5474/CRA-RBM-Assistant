import { RiskSite } from "@/types/risk";

export interface RiskLevelCounts {
	high: number;
	medium: number;
	low: number;
}

export function getRiskLevelCounts(sites: RiskSite[]): RiskLevelCounts {
	return {
		high: sites.filter((site) => site.riskLevel === "High").length,
		medium: sites.filter((site) => site.riskLevel === "Medium").length,
		low: sites.filter((site) => site.riskLevel === "Low").length,
	};
}
