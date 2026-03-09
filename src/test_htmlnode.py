import unittest
from htmlnode import HTMLNode

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