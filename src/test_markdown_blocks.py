import unittest

from markdown_blocks import markdown_to_blocks, BlockType
from markdown_blocks import block_to_block_type


class MarkdownBlocksTest(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(BlockType.HEADING, block_to_block_type("# This is a heading"))
        self.assertEqual(BlockType.CODE, block_to_block_type("```This is code```"))
        self.assertEqual(BlockType.QUOTE, block_to_block_type("> This is a quote"))
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type("- This is a list"))
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type("1. This is a list\n2. with items"))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type("This is a paragraph"))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type("1. This is a list\n2. with items\n- but this is not an ordered list"))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type("1. This is a list\n3. with items"))



if __name__ == '__main__':
    unittest.main()
