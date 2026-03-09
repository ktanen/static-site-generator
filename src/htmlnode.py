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