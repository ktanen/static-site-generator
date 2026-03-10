from textnode import TextNode, TextType

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