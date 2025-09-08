from enum  import Enum
from htmlnode import LeafNode

class TextNodeType(Enum):
    TEXT = "text"
    PLAIN= "plain"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    CODE = "code"
    IMAGE = "image"
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextNodeType(text_type)
        self.url = url
        
    def __eq__(self, other):
        if self.text  == other.text and self.text_type == other.text_type and self.url == other.url:
            return True    
    
    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"
    

def text_node_to_html(text_node):
    if text_node.text_type == TextNodeType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextNodeType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextNodeType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextNodeType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextNodeType.LINK:
        return LeafNode("a",text_node.text, {"href": text_node.url})
    if text_node.text_type == TextNodeType.IMAGE:
        return LeafNode("img","", {"src":text_node.url, "alt":text_node.text})
    raise ValueError(f"Invalid type {text_node.text_type}")
        
    
    

    