import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
	def test_text_to_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		
		self.assertEqual(len(new_nodes), 3)
		
		self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
		self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
		self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

if __name__ == "__main__":
	unittest.main()
