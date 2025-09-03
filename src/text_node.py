from enum  import Enum

class TextNodeType(Enum):
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
    
    

    