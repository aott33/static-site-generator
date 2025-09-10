def markdown_to_blocks(markdown):
	md_blocks = []
	md_split = markdown.split('\n\n')

	for md_block in md_split:
		if not md_block:
			continue

		md_blocks.append(md_block.strip())

	return md_blocks
