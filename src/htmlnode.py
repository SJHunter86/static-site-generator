class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("Children of HTMLNode must implement this class.")
    
    def props_to_html(self):
        if self.props:
            prop_text = ""
            for key, value in self.props.items():
                prop_text += f"{key}=\"{value}\" "
            prop_text = prop_text.rstrip()
            return prop_text