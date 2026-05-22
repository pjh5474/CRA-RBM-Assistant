interface TextSectionProps {
	title: string;
	content: string;
}

export function TextSection({ title, content }: TextSectionProps) {
	return (
		<section>
			<h4 className="mb-2 text-sm font-bold text-slate-900">{title}</h4>
			<p className="whitespace-pre-line rounded-xl bg-slate-50 p-4 text-sm leading-6 text-slate-700">
				{content}
			</p>
		</section>
	);
}
