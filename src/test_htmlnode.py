import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
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
    def test_no_children(self):
        parent_node = ParentNode("div",None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_multiple_leaf_children(self):
        first_child_node = LeafNode("b", "child1")
        second_child_node = LeafNode(None, "child2")
        third_child_node = LeafNode("i", "child3")
        leaves = [first_child_node, second_child_node, third_child_node]
        parent_node = ParentNode("p",leaves)
        expected = "<p><b>child1</b>child2<i>child3</i></p>"
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_empty_child_list(self):
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), "<p></p>")