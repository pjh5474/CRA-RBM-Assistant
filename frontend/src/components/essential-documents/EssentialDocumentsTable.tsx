import { DocumentStatusBadge } from "@/components/essential-documents/DocumentStatusBadge";
import { EssentialDocument } from "@/types/essentialDocument";

interface EssentialDocumentsTableProps {
	documents: EssentialDocument[];
}

export function EssentialDocumentsTable({
	documents,
}: EssentialDocumentsTableProps) {
	return (
		<section className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
			<div className="border-b border-slate-200 p-5">
				<h2 className="text-lg font-bold text-slate-900">
					Essential Document List
				</h2>
				<p className="mt-1 text-sm text-slate-600">
					Required site documents and their current readiness status.
				</p>
			</div>

			<div className="overflow-x-auto">
				<table className="w-full min-w-[900px] text-left text-sm">
					<thead className="bg-slate-50 text-xs uppercase tracking-wide text-slate-500">
						<tr>
							<th className="px-5 py-3">Document Type</th>
							<th className="px-5 py-3">Status</th>
							<th className="px-5 py-3">Version</th>
							<th className="px-5 py-3">Document Date</th>
							<th className="px-5 py-3">Expiry Date</th>
							<th className="px-5 py-3">Comment</th>
						</tr>
					</thead>
					<tbody className="divide-y divide-slate-100">
						{documents.map((document) => (
							<tr key={document.documentId} className="align-top">
								<td className="px-5 py-4">
									<p className="font-semibold text-slate-900">
										{document.documentType}
									</p>
									<p className="mt-1 text-xs text-slate-500">
										{document.documentId}
									</p>
								</td>
								<td className="px-5 py-4">
									<DocumentStatusBadge status={document.status} />
								</td>
								<td className="px-5 py-4 text-slate-700">
									{document.version ?? "N/A"}
								</td>
								<td className="px-5 py-4 text-slate-700">
									{document.documentDate ?? "N/A"}
								</td>
								<td className="px-5 py-4 text-slate-700">
									{document.expiryDate ?? "N/A"}
								</td>
								<td className="px-5 py-4 text-slate-700">
									{document.comment ?? "No comment"}
								</td>
							</tr>
						))}
					</tbody>
				</table>
			</div>
		</section>
	);
}
