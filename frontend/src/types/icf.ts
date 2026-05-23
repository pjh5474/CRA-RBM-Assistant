export interface IcfVersion {
	icfVersionId: string;
	studyId: string;
	version: string;
	irbApprovalDate: string;
	effectiveDate: string;
	status: "Active" | "Superseded";
}

export interface SubjectConsent {
	consentId: string;
	studyId: string;
	siteId: string;
	subjectCode: string;
	signedIcfVersion: string;
	consentDate: string;
	consentProcessNote?: string | null;
}

export interface IcfVersionCheckItem {
	consentId: string;
	subjectCode: string;
	signedIcfVersion: string;
	consentDate: string;
	expectedIcfVersion?: string | null;
	status: "Valid" | "Issue";
	issueType?: string | null;
	message: string;
}

export interface IcfVersionCheck {
	studyId: string;
	siteId: string;
	siteName: string;
	totalConsents: number;
	validConsents: number;
	issueConsents: number;
	icfVersions: IcfVersion[];
	consents: SubjectConsent[];
	checks: IcfVersionCheckItem[];
}
