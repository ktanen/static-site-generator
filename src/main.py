import os
import os.path
import shutil


def copy_files_recursive(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    for entry in os.listdir(source):
        from_path = os.path.join(source,entry)
        dest_path = os.path.join(dest, entry)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path,dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_files_recursive("static", "public")

main()