from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_blocktype, BlockType
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
from leafnode import text_node_to_html_node
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    parent = ParentNode('div', [])
    
    for block in blocks:
        block_type = block_to_blocktype(block)
        children = []
        if block_type == BlockType.CODE:
            formatted = '\n'.join(block.split('\n')[1:-1])
            text_node = TextNode(formatted, TextType.TEXT)
            children = [text_node_to_html_node(text_node)]
        else:
            children = text_to_children(block)

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

