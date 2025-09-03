import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello World" , None,{"class": "greeting", "href": "https://boot.dev"},)
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"',)
        
    def test_values(self):
        node = HTMLNode("div","I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_repr(self):
        node = HTMLNode("p", "What a strange World", None, {"class":"primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(tag=p, value=What a strange World, children=None, props={'class': 'primary'})")
        
if __name__ == "__main__":
    unittest.main()
        
            