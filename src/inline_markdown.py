from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text
            text_chunks = node_text.split(delimiter)
            if len(text_chunks) % 2 == 0:
                raise Exception("invalid Markdown syntax: unbalanced delimiters")
            for i in range(len(text_chunks)):
                chunk = text_chunks[i]
                if chunk:
                    if i % 2 == 0:
                        new_node = TextNode(chunk,TextType.TEXT)
                    else:
                        new_node = TextNode(chunk,text_type)
                    new_nodes.append(new_node)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:

            node_text = node.text
            images = extract_markdown_images(node_text)

            if len(images) == 0:
                new_nodes.append(node)
                continue
            
            for image in images:
                image_alt, image_link = image

                sections = node_text.split(f"![{image_alt}]({image_link})", 1)
                before = sections[0]
                after = sections[1]
                
                if before:
                    before_node = TextNode(before,TextType.TEXT)
                    new_nodes.append(before_node)
                image_node = TextNode(image_alt, TextType.IMAGE, image_link)
                new_nodes.append(image_node)
                node_text = after

            if node_text:
                last_after_node = TextNode(node_text, TextType.TEXT)
                new_nodes.append(last_after_node)                
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text
            links = extract_markdown_links(node_text)

            if len(links) == 0:
                new_nodes.append(node)
                continue
            
            for link in links:
                link_text, link_url = link
                sections = node_text.split(f"[{link_text}]({link_url})", 1)
                before = sections[0]
                after = sections[1]
                
                if before:
                    before_node = TextNode(before,TextType.TEXT)
                    new_nodes.append(before_node)
                link_node = TextNode(link_text, TextType.LINK, link_url)
                new_nodes.append(link_node)
                node_text = after

            if node_text:
                last_after_node = TextNode(node_text, TextType.TEXT)
                new_nodes.append(last_after_node) 

    return new_nodes