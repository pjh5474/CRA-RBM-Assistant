import Link from "next/link";
import { getAuditLogs } from "@/lib/api";
import { AuditLog } from "@/types/auditLog";

export default async function AuditLogsPage() {
	const logs = await getAuditLogs({ limit: 50 });

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className="mx-auto max-w-7xl space-y-8">
				<div>
					<Link href="/" className="text-sm font-medium text-blue-700">
						← Back to study list
					</Link>
				</div>

				<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
					<p className="mb-2 text-sm font-semibold text-blue-700">
						Trigger-based Audit-like Logs
					</p>
					<h1 className="text-2xl font-bold text-slate-900">
						Data Change Traceability
					</h1>
					<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
						This page displays table-level insert, update, and delete events
						recorded by PostgreSQL triggers. It demonstrates data change
						traceability for portfolio purposes and is not a validated
						regulatory audit trail.
					</p>
				</section>

				<section className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
					<div className="border-b border-slate-200 p-5">
						<h2 className="text-lg font-bold text-slate-900">
							Recent Audit Logs
						</h2>
					</div>

					<div className="overflow-x-auto">
						<table className="w-full min-w-[1000px] text-left text-sm">
							<thead className="bg-slate-50 text-xs uppercase tracking-wide text-slate-500">
								<tr>
									<th className="px-5 py-3">Time</th>
									<th className="px-5 py-3">Table</th>
									<th className="px-5 py-3">Action</th>
									<th className="px-5 py-3">Record ID</th>
									<th className="px-5 py-3">Changed Fields</th>
									<th className="px-5 py-3">Actor</th>
								</tr>
							</thead>
							<tbody className="divide-y divide-slate-100">
								{logs.map((log) => (
									<tr key={log.id} className="align-top">
										<td className="px-5 py-4 text-slate-600">
											{formatDateTime(log.createdAt)}
										</td>
										<td className="px-5 py-4 font-medium text-slate-900">
											{log.tableName}
										</td>
										<td className="px-5 py-4">
											<ActionBadge action={log.action} />
										</td>
										<td className="px-5 py-4 text-slate-700">{log.recordId}</td>
										<td className="px-5 py-4">
											<ChangedFields log={log} />
										</td>
										<td className="px-5 py-4 text-slate-500">
											{log.actorUserId ?? "System / service role"}
										</td>
									</tr>
								))}
							</tbody>
						</table>
					</div>
				</section>
			</div>
		</main>
	);
}

function ActionBadge({ action }: { action: AuditLog["action"] }) {
	const className =
		action === "INSERT"
			? "bg-emerald-50 text-emerald-700"
			: action === "UPDATE"
				? "bg-blue-50 text-blue-700"
				: "bg-red-50 text-red-700";

	return (
		<span
			className={`rounded-full px-3 py-1 text-xs font-semibold ${className}`}
		>
			{action}
		</span>
	);
}

function ChangedFields({ log }: { log: AuditLog }) {
	const fields = getChangedFields(log);

	if (fields.length === 0) {
		return (
			<span className="text-slate-400">No field comparison available</span>
		);
	}

	return (
		<div className="flex flex-wrap gap-2">
			{fields.slice(0, 8).map((field) => (
				<span
					key={field}
					className="rounded-full bg-slate-100 px-2 py-1 text-xs font-medium text-slate-700"
				>
					{field}
				</span>
			))}
			{fields.length > 8 && (
				<span className="text-xs text-slate-500">
					+{fields.length - 8} more
				</span>
			)}
		</div>
	);
}

function getChangedFields(log: AuditLog): string[] {
	if (log.action === "INSERT" && log.newData) {
		return Object.keys(log.newData);
	}

	if (log.action === "DELETE" && log.oldData) {
		return Object.keys(log.oldData);
	}

	if (log.action === "UPDATE" && log.oldData && log.newData) {
		const keys = new Set([
			...Object.keys(log.oldData),
			...Object.keys(log.newData),
		]);

		return Array.from(keys).filter((key) => {
			return (
				JSON.stringify(log.oldData?.[key]) !==
				JSON.stringify(log.newData?.[key])
			);
		});
	}

	return [];
}

function formatDateTime(value: string) {
	return new Intl.DateTimeFormat("en-US", {
		dateStyle: "medium",
		timeStyle: "short",
	}).format(new Date(value));
}
