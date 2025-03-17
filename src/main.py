from generate_page import generate_page
import os
import shutil

def main():
    copy_static()

def copy_static():
    source_dir = "static"
    destination_dir = "public"

    # Delete all contents of the destination directory
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Copy all files and subdirectories
    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            source_path = os.path.join(root, dir_name)
            destination_path = os.path.join(destination_dir, os.path.relpath(source_path, source_dir))
            os.makedirs(destination_path, exist_ok=True)
            print(f"Created directory: {destination_path}")
        for file_name in files:
            source_path = os.path.join(root, file_name)
            destination_path = os.path.join(destination_dir, os.path.relpath(source_path, source_dir))
            shutil.copy2(source_path, destination_path)
            print(f"Copied file: {source_path} to {destination_path}")

    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")


if __name__ == "__main__":
    main()
