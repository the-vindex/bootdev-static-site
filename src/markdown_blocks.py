import re
from enum import Enum


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))
    return blocks

def block_to_block_type(text):
    if re.match(r"^(#+)\s", text):
        return BlockType.HEADING
    if re.match(r"^```", text):
        return BlockType.CODE
    if re.match(r"^>\s", text):
        return BlockType.QUOTE
    if re.match(r"^-", text):
        return BlockType.UNORDERED_LIST
    if re.match(r"\d+\.\s", text):
        #this is candidate for numbered list, but must check further
        #Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if not re.match(rf"^{i+1}\.\s", line):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


# input: block of type BlockType.HEADING
# returns: block_text, heading level
def parse_block_heading(block_text):
    level = block_text.count("#", 0, 6)
    title = block_text.replace("#", "").lstrip()
    return level, title
