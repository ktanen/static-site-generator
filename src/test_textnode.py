import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_one_missing_url(self):
        node = TextNode("This is a text node.", TextType.LINK)
        node2 = TextNode("This is a text node.", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_link(self):
        # 1. Create a TextNode with a link type and a URL
        node = TextNode("Click me!", TextType.LINK, "https://www.boot.dev")
        
        # 2. Convert it using your new function
        html_node = text_node_to_html_node(node)
        
        # 3. Assert the details match a LeafNode <a> tag
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me!")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_text_node_to_html_node_invalid(self):
        # Create a node with a type that isn't in your TextType enum 
        # (or just a plain string if your function doesn't strictly check the enum)
        node = TextNode("Bad node", "not_a_type")
        
        # This checks that calling your function raises an Exception
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_image(self):
        node = TextNode("Test",TextType.IMAGE,"https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {"src": "https://www.example.com", "alt": "Test"})
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
if __name__ == "__main__":
    unittest.main()