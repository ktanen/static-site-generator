import os
import os.path
from extract_title import extract_title
from block_markdown import markdown_to_html_node
from pathlib import Path

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generatiing page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()
    
    with open(template_path) as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    full_html = full_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    full_content_path = Path(dir_path_content)
    full_template_path = Path(template_path)
    full_dest_dir_path = Path(dest_dir_path)

    for entry in full_content_path.iterdir():
        if entry.is_file() and str(entry).endswith(".md"):
            full_dest_dir_path.mkdir(parents=True, exist_ok=True)
            final_filepath = (full_dest_dir_path / entry.name).with_suffix(".html")
            
            generate_page(entry, full_template_path, final_filepath, basepath)
        elif entry.is_dir():
            generate_pages_recursive(entry, full_template_path, full_dest_dir_path / entry.name, basepath)