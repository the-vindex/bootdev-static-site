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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    page_markdown = Path(from_path).read_text()
    template_text = Path(template_path).read_text()
    title = extract_title(page_markdown)
    html_node_tree = markdown_to_html_node(page_markdown)
    html_string = html_node_tree.to_html()
    template_text = template_text.replace("{{ Title }}", title)
    template_text = template_text.replace("{{ Content }}", html_string)

    create_folder_and_write_file(dest_path, template_text)


def create_folder_and_write_file(dest_path, template_text):
    dest_file = Path(dest_path)
    dest_dir = dest_file.parent
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest_file.write_text(template_text)


