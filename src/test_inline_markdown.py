import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_delim_code(self):
        node = TextNode("This is text with a `code` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_multiple_delims(self):
        node = TextNode("This is **text** with **two** bolded words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ",TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with ",TextType.TEXT),
                TextNode("two", TextType.BOLD),
                TextNode(" bolded words",TextType.TEXT),

            ],
            new_nodes,
        )
    def test_delims_start_end(self):
        node = TextNode("`code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual([TextNode("code",TextType.CODE)], new_nodes)
    
    def test_no_delims(self):
        node = TextNode("This text has no delimiters or formatting.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual([node], new_nodes)
    def test_delim_bold_error(self):
        node = TextNode("This is text with an **unbalanced delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ",TextType.TEXT),
            TextNode("to boot dev",TextType.LINK,"https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube",TextType.LINK,"https://www.youtube.com/@bootdotdev")            
        ]
        self.assertListEqual(new_nodes, expected)

    def test_link_split_plain_text(self):
        node = TextNode("plain text",TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [node]
        self.assertListEqual(new_nodes, expected)

    def test_image_split_plain_text(self):
        node = TextNode("plain text",TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [node]
        self.assertListEqual(new_nodes, expected)

    def test_split_links_mixed(self):
        # One bold node (should be ignored) and one text node with a link
        nodes = [
            TextNode("bold item", TextType.BOLD),
            TextNode("Link here [to boot](https://www.boot.dev)", TextType.TEXT),
        ]
        
        new_nodes = split_nodes_link(nodes)
        
        # We expect the BOLD node to remain exactly the same, 
        # followed by the split pieces of the second node.
        self.assertListEqual(
            [
                TextNode("bold item", TextType.BOLD),
                TextNode("Link here ", TextType.TEXT),
                TextNode("to boot", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )
    
    def test_split_images_mixed(self):
        nodes = [
            TextNode("italic item", TextType.ITALIC),
            TextNode("Image ![here](https://boot.dev/img.png)",TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("italic item", TextType.ITALIC),
            TextNode("Image ",TextType.TEXT),
            TextNode("here",TextType.IMAGE,"https://boot.dev/img.png"),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_start_image(self):
        node = TextNode("![img](https://boot.dev/img.png) and then text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("img",TextType.IMAGE,"https://boot.dev/img.png"),
            TextNode(" and then text",TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_end_image(self):
        node = TextNode("Text and then ![img](https://boot.dev/img.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Text and then ",TextType.TEXT),
            TextNode("img",TextType.IMAGE,"https://boot.dev/img.png"),
        ]
        self.assertListEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()