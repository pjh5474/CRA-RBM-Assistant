interface DelegationTrainingHeaderProps {
	siteName: string;
}

export function DelegationTrainingHeader({
	siteName,
}: DelegationTrainingHeaderProps) {
	return (
		<section className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
			<p className="mb-2 text-sm font-semibold text-blue-700">
				Delegation & Training Log Check
			</p>

			<h1 className="text-2xl font-bold text-slate-900">{siteName}</h1>

			<p className="mt-3 max-w-4xl text-sm leading-6 text-slate-600">
				This page checks whether delegated site staff completed GCP and protocol
				training before their delegation start date. It demonstrates CRA-oriented
				review of delegation log and training evidence consistency.
			</p>
		</section>
	);
}
