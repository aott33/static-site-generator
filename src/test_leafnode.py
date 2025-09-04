import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a1(self):
        node = LeafNode('a', 'this is a link', {'href': 'https://www.google.com', 'target': '_blank',})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">this is a link</a>')
    def test_leaf_to_html_a2(self):
        node = LeafNode('a', 'this is a link', {'href': 'https://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">this is a link</a>')

if __name__ == "__main__":
    unittest.main()
