from enum import Enum


from leafnode import LeafNode

import re

def text_node_to_html_node(node):
    match node.text_type:
        case TextType.TEXT:
            return LeafNode(None, node.text)
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            return LeafNode("a", node.text, props={"href": node.url})
        case TextType.IMAGE:
            return LeafNode("img", None, props={"src": node.url, "alt": node.text})
        case _:
            raise ValueError("Unknown node type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            if not part:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def __create_image_markdown(image_tuple):
    return f"![{image_tuple[0]}]({image_tuple[1]})"

def __create_image_node(image_tuple_text_url):
    return TextNode(image_tuple_text_url[0], TextType.IMAGE, image_tuple_text_url[1])

def split_nodes_image(old_nodes):
    return __split_nodes_internal(old_nodes, extract_markdown_images, __create_image_markdown, __create_image_node)


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def __create_link_markdown(tuple_alt_img):
    return f"[{tuple_alt_img[0]}]({tuple_alt_img[1]})"

def __create_link_node(link_tuple_text_url):
    return TextNode(link_tuple_text_url[0], TextType.LINK, link_tuple_text_url[1])



def split_nodes_link(old_nodes):
    return __split_nodes_internal(old_nodes, extract_markdown_links, __create_link_markdown, __create_link_node)

def __split_nodes_internal(old_nodes, extract_markdown_func, rebuild_text_func, create_node_func):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        image_tuples = extract_markdown_func(node_text)
        if not image_tuples:
            new_nodes.append(node)
            continue
        else:
            for image_tuple in image_tuples:
                #split the text into before and after the node we are extracting
                node_text_before_and_after_url = node_text.split(rebuild_text_func(image_tuple))
                node_text_before_url: str = node_text_before_and_after_url[0]
                node_text_after_url: str = node_text_before_and_after_url[1]

                #text before, if any
                if len(node_text_before_url) > 0:
                    new_nodes.append(TextNode(node_text_before_url, TextType.TEXT))

                new_nodes.append(create_node_func(image_tuple))

                #text after, if any, will go into the next loop
                node_text = node_text_after_url

            if len(node_text) > 0:
                new_nodes.append(TextNode(node_text, TextType.TEXT))

    return new_nodes




class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = 'code'
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

