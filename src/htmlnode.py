class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Implementation to convert node to HTML string
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        # Implementation to convert node properties to a dictionary
        for prop, value in self.props.items():
            yield f' {prop}="{value}"'

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
