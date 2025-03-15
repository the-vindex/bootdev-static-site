from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is mandatory for ParentNode")
        if not self.children:
            raise ValueError("children is mandatory for ParentNode")

        html = ""
        for child in self.children:
            html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"

