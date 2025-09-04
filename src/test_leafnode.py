import unittest
from leafnode import LeafNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	def test_leaf_to_html_a(self):
		node = LeafNode('a', 'this is a link', {'href': 'https://www.google.com', 'target': '_blank',})
		self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="blank">this is a link</a>')
	def test_leaf_to_html_a(self):
		node = LeafNode('a', 'this is a link', {'href': 'https://www.google.com'})
		self.assertEqual(node.to_html(), '<a href="https://www.google.com">this is a link</a>')
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
	unittest.main()
