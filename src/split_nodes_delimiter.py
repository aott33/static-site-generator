from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	updated_nodes = []

	if text_type not in TextType:
		raise Exception(f'{text_type} not defined in the TextType')

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			updated_nodes.append(node)

		elif delimiter in node.text:
			node_text_split = node.text.split(delimiter)

			parsed_nodes_updated = []

			if len(node_text_split) % 2 == 0:
				raise Exception(f'"{node.txt}" does not contain closing delimiter')

			for i in range(0,len(node_text_split)):
				if i % 2 == 0 or i == 0:
					parsed_nodes_updated.append(TextNode(node_text_split[i], TextType.TEXT))
				else:
					parsed_nodes_updated.append(TextNode(node_text_split[i], text_type))

			updated_nodes.extend(parsed_nodes_updated)
		else:
			updated_nodes.append(node)
	return updated_nodes
