import os
import os.path
import shutil
from copystatic import copy_files_recursive
from page_generator import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_files_recursive("static", "public")

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()