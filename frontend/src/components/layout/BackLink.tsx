import Link from "next/link";

interface BackLinkProps {
	href: string;
	children: React.ReactNode;
}

export function BackLink({ href, children }: BackLinkProps) {
	return (
		<Link href={href} className="text-sm font-medium text-blue-700">
			{children}
		</Link>
	);
}
