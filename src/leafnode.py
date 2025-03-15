from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if  not self.value:
            raise ValueError

        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return self.value
