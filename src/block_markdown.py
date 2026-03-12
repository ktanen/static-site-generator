from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode
from blocktype import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = []

    potential_blocks = markdown.split("\n\n")
    
    for block in potential_blocks:
        block = block.strip()
        if block:
            blocks.append(block)

    return blocks

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def create_quote_node(text):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_line = line.lstrip(">").lstrip()
        cleaned_lines.append(cleaned_line)
    cleaned_text = " ".join(cleaned_lines)
    children = text_to_children(cleaned_text)
    quote_node = ParentNode("blockquote",children)
    return quote_node

def create_paragraph_node(text):
    cleaned_text = text.replace("\n", " ")
    children = text_to_children(cleaned_text)
    paragraph_node = ParentNode("p", children)
    return paragraph_node

def create_heading_node(text):
    level = len(text) - len(text.lstrip("#"))
    cleaned_text = text[level + 1:]
    children = text_to_children(cleaned_text)
    heading_node = ParentNode(f"h{level}",children)
    return heading_node

def create_unordered_list_node(text):
    lines = text.split("\n")
    list_items = []
    for line in lines:
        cleaned_line = line[2:]
        children = text_to_children(cleaned_line)
        item_node = ParentNode("li", children)
        list_items.append(item_node)
    
    list_node = ParentNode("ul", list_items)
    return list_node

def create_ordered_list_node(text):
    lines = text.split("\n")
    list_items = []
    for line in lines:
        cleaned_line = line.split(". ", 1)[1]
        children = text_to_children(cleaned_line)
        item_node = ParentNode("li", children)
        list_items.append(item_node)
    list_node = ParentNode("ol", list_items)
    return list_node

def create_code_node(text):
    cleaned_text = text[4:-3]
    text_node = TextNode(cleaned_text,TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    code_node = ParentNode("code", [html_node])
    pre_node = ParentNode("pre", [code_node])
    return pre_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                block_node = create_paragraph_node(block)
            case BlockType.HEADING:
                block_node = create_heading_node(block)
            case BlockType.CODE:
                block_node = create_code_node(block)
            case BlockType.QUOTE:
                block_node = create_quote_node(block)
            case BlockType.UNORDERED_LIST:
                block_node = create_unordered_list_node(block)
            case BlockType.ORDERED_LIST:
                block_node = create_ordered_list_node(block)
            case _:
                raise ValueError("invalid block type")
                
        block_nodes.append(block_node)

    
    parent_node = ParentNode("div", block_nodes)
    return parent_node
            