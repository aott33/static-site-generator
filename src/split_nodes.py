from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_images(old_nodes):
	updated_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			updated_nodes.append(node)

		else:
			regex_list = extract_markdown_images(node.text)
			
			if len(regex_list) > 0:
				parsed_nodes_updated = []

				current_text = node.text

				for regex_tuple in regex_list:
					image_alt = regex_tuple[0]
					image_link = regex_tuple[1]
					
					sections = current_text.split(f"![{image_alt}]({image_link})", 1)
					
					if sections[0] != '':
						parsed_nodes_updated.append(TextNode(sections[0], TextType.TEXT))

					parsed_nodes_updated.append(TextNode(image_alt, TextType.IMAGE, image_link))
					

					current_text = sections[1]

					if regex_tuple == regex_list[len(regex_list)-1] and sections[1]:
						parsed_nodes_updated.append(TextNode(sections[1], TextType.TEXT))

				updated_nodes.extend(parsed_nodes_updated)

			else:
				updated_nodes.append(node)

	return updated_nodes

def split_nodes_links(old_nodes):

	updated_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT and node.text != '':
			updated_nodes.append(node)

		else:
			regex_list = extract_markdown_links(node.text)
			if len(regex_list) > 0:
				parsed_nodes_updated = []

				current_text = node.text

				for regex_tuple in regex_list:
					text = regex_tuple[0]
					link = regex_tuple[1]
					
					sections = current_text.split(f"[{text}]({link})", 1)
					
					if sections[0] != '':
						parsed_nodes_updated.append(TextNode(sections[0], TextType.TEXT))
	
					parsed_nodes_updated.append(TextNode(text, TextType.LINK, link))
					

					current_text = sections[1]

				updated_nodes.extend(parsed_nodes_updated)

			else:
				updated_nodes.append(node)

	return updated_nodes
