import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class ParentNodeNode(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)
	def test_to_html_with_multiple_children(self):
		child_node1 = LeafNode("b", "Bold Text")
		child_node2 = LeafNode(None, "Normal Text")
		child_node3 = LeafNode("i", "Italic Text")
		child_node4 = LeafNode(None, "Normal Text")
		parent_node = ParentNode("p", [child_node1, child_node2, child_node3, child_node4])
		self.assertEqual(
			parent_node.to_html(),
			"<p><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal Text</p>",
		)
	def test_to_html_with_multiple_children_and_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node1 = ParentNode("span", [grandchild_node])
		child_node2 = LeafNode(None, "Normal Text")
		child_node3 = LeafNode("i", "Italic Text")
		child_node4 = LeafNode(None, "Normal Text")
		parent_node = ParentNode("p", [child_node1, child_node2, child_node3, child_node4])
		self.assertEqual(
			parent_node.to_html(),
			"<p><span><b>grandchild</b></span>Normal Text<i>Italic Text</i>Normal Text</p>",
		)
		
	def test_to_html_with_multiple_children_and_grandchildren_and_props(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node1 = ParentNode("span", [grandchild_node])
		child_node2 = LeafNode(None, "Normal Text")
		child_node3 = LeafNode("i", "Italic Text")
		child_node4 = LeafNode(None, "Normal Text")
		child_node5 = LeafNode("a", 'this is a link', {'href': 'https://www.google.com', 'target': '_blank',})
		parent_node = ParentNode("p", [child_node1, child_node2, child_node3, child_node4, child_node5])
		self.assertEqual(
			parent_node.to_html(),
			'<p><span><b>grandchild</b></span>Normal Text<i>Italic Text</i>Normal Text<a href="https://www.google.com" target="_blank">this is a link</a></p>',
		)

if __name__ == "__main__":
	unittest.main()
