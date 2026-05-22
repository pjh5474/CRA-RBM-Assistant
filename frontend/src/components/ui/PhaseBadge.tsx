interface PhaseBadgeProps {
	phase: string;
}

export function PhaseBadge({ phase }: PhaseBadgeProps) {
	return (
		<span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700">
			{phase}
		</span>
	);
}
