import unittest
from block_markdown import markdown_to_blocks, markdown_to_html_node

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_extra_spaces(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_strip(self):
        md = """
    This is **bolded** paragraph   

    This is another paragraph   
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph",
            ],
        )

        # Markdown to HTML test
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_1(self):
        md = "# Test"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Test</h1></div>"
        )

    def test_heading_2(self):
        md = "## Test"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Test</h2></div>"
        )
    
    def test_heading_3(self):
        md = "### Test"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Test</h3></div>"
        )

    def test_heading_4(self):
        md = "#### Test"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>Test</h4></div>"
        )

    def test_heading_5(self):
        md = "##### Test"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>Test</h5></div>"
        )


    def test_heading_6(self):
        md = "###### Test"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>Test</h6></div>"
        )
    def test_quote(self):
        md = """
>In the morning I'll be sober,
>and you'll still be ugly.
        """
        node = markdown_to_html_node(md)
        html  = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>In the morning I'll be sober, and you'll still be ugly.</blockquote></div>"
        )
    def test_unordered_list(self):
        md = """
- Ketchup
- Mustard
- Relish
        """
        node = markdown_to_html_node(md)
        html  = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Ketchup</li><li>Mustard</li><li>Relish</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. Ketchup
2. Mustard
3. Relish
        """
        node = markdown_to_html_node(md)
        html  = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Ketchup</li><li>Mustard</li><li>Relish</li></ol></div>"
        )

if __name__ == "__main__":
    unittest.main()