def markdown_to_blocks(markdown):
    blocks = []
    print(repr(markdown))
    for chunk in markdown.split("\n\n"):
        block = chunk.strip()
        if block:
            blocks.append(block)
    return blocks
