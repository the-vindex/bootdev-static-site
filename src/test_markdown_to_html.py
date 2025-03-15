import unittest

from markdown_to_html import markdown_to_html_node


class MarkdownToHtmlTest(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            html,
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# This is a heading

## This is a **smaller** heading

### This is an even smaller heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><h1>This is a heading</h1><h2>This is a <b>smaller</b> heading</h2><h3>This is an even smaller heading</h3></div>",
            html,
        )

    def test_quote(self):
        md = """> This is a quote
> with multiple lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><blockquote>This is a quote with multiple lines</blockquote></div>",
            html,
        )

    def test_unnumbered_list(self):
        md = """
- This is a list
- with items
- and more items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><ul><li>This is a list</li><li>with items</li><li>and more items</li></ul></div>",
            html,
        )

    def test_ordered_list(self):
        md = """
1. This is a list
2. with items
3. and more items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><ol><li>This is a list</li><li>with items</li><li>and more items</li></ol></div>",
            html,
        )



if __name__ == '__main__':
    unittest.main()
