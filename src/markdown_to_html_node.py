from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_blocktype, BlockType
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
from leafnode import text_node_to_html_node
from parentnode import ParentNode
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    parent = ParentNode('div', [])

    for block in blocks:
        block_type = block_to_blocktype(block)
        children = []
        if block_type == BlockType.CODE:
            inner_lines = block.split("\n")[1:-1]
            common = min((len(l) - len(l.lstrip(" "))) for l in inner_lines if l.strip() != "")
            inner_lines = [l[common:] if len(l) >= common else l for l in inner_lines]
            formatted = "\n".join(inner_lines) + "\n"
            text_node = TextNode(formatted, TextType.CODE)
            children = [text_node_to_html_node(text_node)]

        elif block_type in [BlockType.ORDERED_LIST, BlockType.UNORDERED_LIST]:
            split_list = block.split('\n')
            
            list_children = []

            for list_item in split_list:
                list_item_content = list_item.split(' ', 1)[1]
                list_item_children = text_to_children(list_item_content)
                list_item_node = ParentNode('li', list_item_children)
                list_children.append(list_item_node)
            children = list_children

        elif block_type == BlockType.QUOTE:
            split_list = block.split('\n')
            
            cleaned_lines = []

            for line in split_list:
                cleaned_lines.append(line.split('>', 1)[1].lstrip())

            clean_text = '\n'.join(cleaned_lines)

            children = text_to_children(clean_text)
        
        elif block_type == BlockType.HEADING:
            cleaned_heading = block.split('# ', 1)[1]
            children = text_to_children(cleaned_heading)

        else:
            content = normalize_paragraph(block)
            children = text_to_children(content)

        tag = get_block_type_tag(block_type, block)

        new_node = ParentNode(tag, children)
        
        parent.children.append(new_node)

    return parent

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []

    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))

    return leaf_nodes


def get_block_type_tag(block_type, block):

    if block_type == BlockType.HEADING:
        block_split = block.split(' ', 1)
        heading_num = block_split[0].count('#')

        return f'h{heading_num}'
    else:
        return block_type.value

def normalize_paragraph(text):
    return re.sub(r"\s+", " ", text).strip()
