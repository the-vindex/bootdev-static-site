from generate_page import generate_page
import os
import shutil

from generate_page import generate_pages_recursive


def main():
    source_dir = "static"
    dest_dir = "docs"
    basepath = "/"

    import sys

    if len(sys.argv) > 1:
        dest_dir = sys.argv[1]
        basepath = dest_dir
    else:
        print("No destination directory provided, using default")




    # Delete all contents of the destination directory
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Copy all files and subdirectories
    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            source_path = os.path.join(root, dir_name)
            destination_path = os.path.join(dest_dir, os.path.relpath(source_path, source_dir))
            os.makedirs(destination_path, exist_ok=True)
            print(f"Created directory: {destination_path}")
        for file_name in files:
            source_path = os.path.join(root, file_name)
            destination_path = os.path.join(dest_dir, os.path.relpath(source_path, source_dir))
            shutil.copy2(source_path, destination_path)
            print(f"Copied file: {source_path} to {destination_path}")

    generate_pages_recursive("content", "template.html", dest_dir, basepath)



if __name__ == "__main__":
    main()
