from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
def text_to_textnodes(text):
    base_node = TextNode(text, TextType.TEXT)
    bold_split = split_nodes_delimiter([base_node],"**",TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, "_", TextType.ITALIC)
    code_split = split_nodes_delimiter(italic_split, "`",TextType.CODE)
    image_split = split_nodes_image(code_split)
    link_split = split_nodes_link(image_split)
    return link_split