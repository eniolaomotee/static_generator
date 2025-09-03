import unittest

from text_node import TextNode, TextNodeType


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
        

if __name__ == "__main__":
    unittest.main()
        
    