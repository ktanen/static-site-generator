import re

def extract_markdown_images(text):
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_pattern, text)
    return matches

def extract_markdown_links(text):
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_pattern, text)
    return matches