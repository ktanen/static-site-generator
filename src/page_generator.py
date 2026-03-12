import os
import os.path
from extract_title import extract_title
from block_markdown import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generatiing page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()
    
    with open(template_path) as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)