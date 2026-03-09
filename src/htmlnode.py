class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        else:
            html_props = ""
            for prop in self.props:
                html_props += f' {prop}="{self.props[prop]}"'
            return html_props
    
    def __repr__(self):
        return f"""Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}
        """

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None:
            return self.value
        html_props = self.props_to_html()
        html = f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
        return html

    def __repr__(self):
        return f"""Tag: {self.tag}
        Value: {self.value}
        Props: {self.props}
        """