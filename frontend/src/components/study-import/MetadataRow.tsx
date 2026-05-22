interface MetadataRowProps {
	label: string;
	values: string[];
}

export function MetadataRow({ label, values }: MetadataRowProps) {
	if (values.length === 0) {
		return null;
	}

	return (
		<p className="mt-2 text-xs text-slate-600">
			<span className="font-semibold text-slate-800">{label}: </span>
			{values.slice(0, 3).join(", ")}
			{values.length > 3 ? "..." : ""}
		</p>
	);
}
