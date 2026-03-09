from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            node_text = text_node.text
            node = LeafNode(None,node_text)
            return node
        case TextType.BOLD:
            node_text = text_node.text
            node = LeafNode("b", node_text)
            return node
        case TextType.ITALIC:
            node_text = text_node.text
            node = LeafNode("i", node_text)
            return node
        case TextType.CODE:
            node_text = text_node.text
            node = LeafNode("code", node_text)
            return node
        case TextType.LINK:
            node_text = text_node.text
            url = text_node.url
            props = {"href": url}
            node = LeafNode("a", node_text, props)
            return node
        case TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.text}
            node = LeafNode("img", "", props)
            return node
        case _:
            raise Exception("invalid text type")