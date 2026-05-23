export interface EssentialDocument {
	documentId: string;
	studyId: string;
	siteId: string;
	documentType: string;
	required: boolean;
	status: "Ready" | "Missing" | "Pending" | "Expired";
	version?: string | null;
	documentDate?: string | null;
	expiryDate?: string | null;
	comment?: string | null;
}

export interface EssentialDocumentReadiness {
	studyId: string;
	siteId: string;
	siteName: string;
	readinessScore: number;
	totalDocuments: number;
	readyDocuments: number;
	missingDocuments: number;
	pendingDocuments: number;
	expiredDocuments: number;
	documents: EssentialDocument[];
}
