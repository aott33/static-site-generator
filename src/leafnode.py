from htmlnode import HTMLNode
from textnode import TextType, TextNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node doesn't have a value")

        if self.tag == None:
            return self.value
        
        html_string = f'<{self.tag}' 
        props_html = ''
        if self.props:
            html_string += self.props_to_html()

        html_string += f'>{self.value}</{self.tag}>'

        return html_string

def text_node_to_html_node(text_node):
    tn_type = text_node.text_type

    if tn_type not in TextType:
        raise Exception(f'{tn_type} not defined in the TextType')

    if tn_type == TextType.TEXT or tn_type == TextType.BOLD or tn_type == TextType.ITALIC or tn_type == TextType.CODE:
        return LeafNode(tn_type.value, text_node.text, None)

    elif tn_type == TextType.LINK:
        props = {"href":text_node.url}
        return LeafNode(tn_type.value, text_node.text, props)

    elif tn_type == TextType.IMAGE:
        props = {"src":text_node.url, "alt":text_node.text}
        return LeafNode(tn_type.value, None, props)
