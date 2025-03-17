from pathlib import Path

from markdown_to_html import *

def extract_title(page_markdown):
    blocks = markdown_to_blocks(page_markdown)
    level, title = None, None

    #returns first H1 heading in the page
    for block in blocks:
        block_type = block_to_block_type(block)
        if BlockType.HEADING == block_type:
            parsed_level, parsed_title = parse_block_heading(block)
            if parsed_level == 1:
                level, title = parsed_level, parsed_title
                break

    if title is None:
        raise ValueError("No H1 heading found in the page")

    return title

def generate_page(from_path, template_path, dest_path, basepath = None):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    page_markdown = Path(from_path).read_text()
    template_text = Path(template_path).read_text()
    title = extract_title(page_markdown)
    html_node_tree = markdown_to_html_node(page_markdown)
    html_string = html_node_tree.to_html()
    template_text = template_text.replace("{{ Title }}", title)
    template_text = template_text.replace("{{ Content }}", html_string)
    if basepath is not None:
        template_text = template_text.replace('href="/', f'href="{basepath}')
        template_text = template_text.replace('src="/', f'src="{basepath}')

    create_folder_and_write_file(dest_path, template_text)


def create_folder_and_write_file(dest_path, template_text):
    dest_file = Path(dest_path)
    dest_dir = dest_file.parent
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest_file.write_text(template_text)

def generate_pages_recursive(dir_path_content, template_path, dest_basepath, basepath=None):
    content_root = Path(dir_path_content)
    for root, dirs, files in content_root.walk():
        for file in files:
            if file.endswith(".md"):
                file_path = Path(root) / file
                relative_path = file_path.relative_to(content_root)
                dest_path = Path(dest_basepath) / relative_path.with_suffix(".html")
                generate_page(str(file_path), template_path, str(dest_path), basepath)
