interface PageContainerProps {
	children: React.ReactNode;
	className?: string;
}

export function PageContainer({ children, className }: PageContainerProps) {
	const innerClassName = className
		? `mx-auto max-w-6xl ${className}`
		: "mx-auto max-w-6xl";

	return (
		<main className="min-h-screen bg-slate-50 px-6 py-10">
			<div className={innerClassName}>{children}</div>
		</main>
	);
}
