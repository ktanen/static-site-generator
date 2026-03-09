import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
  

        node = HTMLNode("a","Test", props={
        "href": "https://www.google.com",
        "target": "_blank",
    })

        html_props = node.props_to_html()
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(html_props, expected_result)
    
    def test_none_props(self):
        node = HTMLNode("a", "Test")
        self.assertEqual(node.props_to_html(), "")
    
    def test_empty_props(self):
        node = HTMLNode("a", "Test", props={})
        self.assertEqual(node.props_to_html(), "")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>' )

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Tagless")
        self.assertEqual(node.to_html(), "Tagless")
    
    def test_leaf_no_value(self):
        node = LeafNode("p",None)
        with self.assertRaises(ValueError):
            node.to_html()