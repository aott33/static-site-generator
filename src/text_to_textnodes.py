from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_images, split_nodes_links

def text_to_textnodes(text):
	tn = TextNode(text, TextType.TEXT)
	tn_list1 = (split_nodes_delimiter([tn], '**', TextType.BOLD))
	tn_list2 = (split_nodes_delimiter(tn_list1, '_', TextType.ITALIC))
	tn_list3 = (split_nodes_delimiter(tn_list2, '`', TextType.CODE))
	tn_list4 = (split_nodes_images(tn_list3))
	tn_list5 = (split_nodes_links(tn_list4))
	return tn_list5

