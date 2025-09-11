class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):        
        return "".join(f' {key}="{value}"' for key, value in self.props.items()) if self.props else ""
    
    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)
        
    def to_html(self):
        # Case 1: plain text (no tag, just raw text)
        if self.tag is None:
            if not self.value:
                raise ValueError("invalid HTML: no value")
            return self.value

        # Case 2: self closing tags like <img>, <br> , <hr>
        if self.tag in ["img","br","hr","input","meta","link"]:
            return f"<{self.tag}{self.props_to_html()}/>" 

        
        # Case 3: normal HTML tags with children
        if not self.value:
            raise ValueError("invalid HTML: no value")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)
        
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        
        return f'<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children},{self.props} )"