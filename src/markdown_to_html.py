from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from parentnode import ParentNode
from markdown_blocks import parse_block_heading
from textnode import text_to_textnodes, textnode_list_to_htmlnode_list, TextNode, TextType


# for each line then call text_to_textnodes
# then call text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_lines = block

        parent_node = block_to_html(block_type, block_lines)
        children.append(parent_node)

    return ParentNode("div", children)

def block_to_html(block_type, block_text):
    match block_type:
        case BlockType.PARAGRAPH:
            block_text = block_text.replace("\n", " ")
            textnodes = text_to_textnodes(block_text)
            htmlnodes = textnode_list_to_htmlnode_list(textnodes)
            return ParentNode(tag = "p", children=htmlnodes)
        case BlockType.HEADING:
            level, title = parse_block_heading(block_text)
            textnodes = text_to_textnodes(title)
            htmlnodes = textnode_list_to_htmlnode_list(textnodes)
            return ParentNode(tag = f"h{level}", children=htmlnodes)

        case BlockType.CODE:
            block_text = block_text.replace("```","").lstrip()
            textnodes = [TextNode(block_text, TextType.CODE)]
            htmlnodes = textnode_list_to_htmlnode_list(textnodes)
            return ParentNode(tag = "pre", children=htmlnodes)
        case BlockType.QUOTE:
            block_text = block_text.replace("> ", "").lstrip()
            block_text = block_text.replace("\n", " ")
            textnodes = text_to_textnodes(block_text)
            htmlnodes = textnode_list_to_htmlnode_list(textnodes)
            return ParentNode(tag = "blockquote", children=htmlnodes)

        case BlockType.UNORDERED_LIST:
            lines = block_text.split("\n")
            children = []
            for line in lines:
                line = line.replace("- ", "").lstrip()
                textnodes = text_to_textnodes(line)
                htmlnodes = textnode_list_to_htmlnode_list(textnodes)
                children.append(ParentNode(tag = "li", children=htmlnodes))
            return ParentNode(tag = "ul", children=children)

        case BlockType.ORDERED_LIST:
            lines = block_text.split("\n")
            children = []
            for line in lines:
                line = line.split(". ", 1)[1].lstrip()
                textnodes = text_to_textnodes(line)
                htmlnodes = textnode_list_to_htmlnode_list(textnodes)
                children.append(ParentNode(tag = "li", children=htmlnodes))
            return ParentNode(tag = "ol", children=children)

        case _:
            raise ValueError("Unknown block type")


def wrap_with_node_html_paragraph(children):
    return [ParentNode(tag = "p", children=children)]