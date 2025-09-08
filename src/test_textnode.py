import unittest

from text_node import TextNode, TextNodeType, text_node_to_html


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is some anchor text", TextNodeType.BOLD)
        node2 = TextNode("This is some anchor text", TextNodeType.BOLD)
        self.assertEqual(node, node2)
        
    def test_neq(self):
        node = TextNode("This is some anchor text", TextNodeType.BOLD)
        node2 = TextNode("This is some anchor text", TextNodeType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is some anchor text", TextNodeType.LINK, "https://www.boot.dev")
        self.assertEqual(node.url, "https://www.boot.dev")
    
    def test_urlNone(self):
        node = TextNode("This is some anchor text", TextNodeType.BOLD)
        self.assertIsNone(node.url)
    
    def test_texttype(self):
        node = TextNode("This is some anchor text", TextNodeType.LINK, "https://www.boot.dev")
        self.assertEqual(node.text_type, TextNodeType.LINK)
        
class TestTextNodetoHtmlNode:
    def test_text(self):
        node = TextNode("This is a text node", TextNodeType.TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_image(self):
        node = TextNode("This is an image",TextNodeType.IMAGE, "https://www.boot.dev")
        html_node  = text_node_to_html(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props,{"src": "https://www.boot.dev", "alt": "This is an image"},)
        
    def test_bold(self):
        node = TextNode("This is bold",TextNodeType.BOLD)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag,"b")
        self.asserEqual(html_node.value, "This is bold")
        

if __name__ == "__main__":
    unittest.main()
        
    
    
    

    