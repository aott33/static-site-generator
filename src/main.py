from textnode import TextNode, TextType
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

def main():
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn)
    
    html_node = HTMLNode("a", "Click me!", None, {'href': 'https://www.google.com', 'target': '_blank',})
    print(html_node.props_to_html())

if __name__ == "__main__":
    main()
