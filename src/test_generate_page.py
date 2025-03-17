import unittest
from pathlib import Path
import os

from generate_page import extract_title, generate_page



class GeneratePageTest(unittest.TestCase):

    def test_extract_title_from_page(self):
        self.assertEqual("page title", extract_title("# page title\n\nThis is text"))

    def test_no_h1_raises_exception(self):
        with self.assertRaises(ValueError):
            extract_title("## page title\n\nThis is text")


    def test_check_complex_html(self):
        content_path = "content/index.md"
        template_path = "template.html"
        if os.path.basename(os.getcwd()) == "src":
            content_path = "../" + content_path
            template_path = "../" + template_path
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html", dir="/tmp") as tmp_file:
            dest_path = tmp_file.name
            generate_page(content_path, template_path, dest_path, "BASEPATH")
            output_html = Path(dest_path).read_text()
# Expecting body to contain: html
# Expecting body to contain: <h1>Tolkien Fan Club</h1>
# Expecting body to contain: <li>Gandalf</li>
# Expecting body to contain: <i>didn't ruin it</i>
# Expecting body to contain: <b>I like Tolkien</b>
# Expecting body to contain: <a href
# Expecting body to contain: <li>It can be enjoyed by children and adults alike</li>
# Expecting body to contain: <code>
# Expecting body to contain: <blockquote>"I am in fact a Hobbit in all but size."
            self.assertIn("<html>", output_html)
            self.assertIn("<h1>Tolkien Fan Club</h1>", output_html)
            self.assertIn("<li>Gandalf</li>", output_html)
            self.assertIn("<i>didn't ruin it</i>", output_html)
            self.assertIn("<b>I like Tolkien</b>", output_html)
            self.assertIn("<a href", output_html)
            self.assertIn("<li>It can be enjoyed by children and adults alike</li>", output_html)
            self.assertIn("<code>", output_html)
            self.assertIn("<blockquote>\"I am in fact a Hobbit in all but size.\"", output_html)

if __name__ == '__main__':
    unittest.main()
