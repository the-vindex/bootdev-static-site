import unittest


class HtmlNodeTest(unittest.TestCase):
    def test_props_to_html_empty(self):
        from htmlnode import HTMLNode
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple(self):
        from htmlnode import HTMLNode
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")


if __name__ == '__main__':
    unittest.main()
