import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class MarkdownToTextNodeTestCase(unittest.TestCase):
    def test_split_by_special_character(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)



if __name__ == '__main__':
    unittest.main()
