class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not yet implemented")

    def props_to_html(self):
        str = ""
        if self.props == None:
            return str
        for key in self.props:
            str += f' {key}="{self.props[key]}"'
        return str

    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"

    def __eq__(self, html_node):
        return (self.tag == html_node.tag and self.value == html_node.value and self.children == html_node.children and self.props == html_node.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("to_html leaf method requires value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("to_html parent method requires tag")
        if self.children == None:
            raise ValueError("to_html parent method requires children list")
        str = f"<{self.tag}>"
        for child in self.children:
            str += child.to_html()
        return str + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"