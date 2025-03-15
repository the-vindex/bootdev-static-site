import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is a text node, link, https://www.boot.dev)")

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(LeafNode(None, "This is a text node"), html_node)

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(LeafNode("b", "This is a bold text node"), html_node)

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(LeafNode("i", "This is an italic text node"), html_node)

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(LeafNode("code", "This is a code text node"), html_node)

    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(LeafNode("a", "This is a link text node", props={"href": "https://www.boot.dev"}), html_node)

    def test_image(self):
        node = TextNode("This is alt text", TextType.IMAGE, "https://www.boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(LeafNode("img", None , props={"src": "https://www.boot.dev/image.png", "alt": "This is alt text"}), html_node)



if __name__ == "__main__":
    unittest.main()
