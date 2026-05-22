export interface AuditLog {
	id: number;
	actorUserId?: string | null;
	tableName: string;
	action: "INSERT" | "UPDATE" | "DELETE";
	recordId: string;
	oldData?: Record<string, unknown> | null;
	newData?: Record<string, unknown> | null;
	createdAt: string;
}
