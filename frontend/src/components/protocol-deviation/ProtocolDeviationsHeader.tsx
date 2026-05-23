interface ProtocolDeviationsHeaderProps {
	siteName: string;
}

export function ProtocolDeviationsHeader({
	siteName,
}: ProtocolDeviationsHeaderProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<p className="mb-2 text-sm font-semibold text-blue-700">
				Protocol Deviation Tracker
			</p>

			<h1 className="text-2xl font-bold text-slate-900">{siteName}</h1>

			<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
				This page structures protocol deviation records by category, severity,
				status, root cause, corrective action, and preventive action. It
				demonstrates how CRA monitoring findings can be tracked beyond simple
				deviation counts.
			</p>
		</section>
	);
}
