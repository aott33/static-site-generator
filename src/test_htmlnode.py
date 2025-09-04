import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_child_node(self):
        child_node = HTMLNode('p', 'this is a sub paragraph', None, {'style':'text-align:right'})
        node = HTMLNode('div', None, [child_node], None)
        self.assertEqual(node.children[0].value,child_node.value)

    def test_child_node2(self):
        child_node1 = HTMLNode('p', 'this is a sub paragraph', None, {'style':'text-align:right'})
        child_node2 = HTMLNode('p', 'this is a second sub paragraph', None, {'style':'text-align:left'})
        node = HTMLNode('div', None, [child_node1, child_node2], None)
        self.assertEqual(node.children[1].value,child_node2.value)

    def test_node_props(self):
        node = HTMLNode('a', 'this is a link', None, {'href': 'https://www.google.com', 'target': '_blank',})
        self.assertEqual(node.props['href'],"https://www.google.com")

if __name__ == "__main__":
    unittest.main()
