import unittest


from htmlnode import LeafNode, ParentNode

class TestLeaf(unittest.TestCase):
    def test_leafnode(self):
        node = LeafNode("p","Hello,world!")
        self.assertEqual(node.to_html(), "<p>Hello,world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None,"Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
        
        
class TestParentNode(unittest.TestCase):
    def test_parentnode(self):
        child_node = LeafNode("span","child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    # def test_to_html_with_grandchildren(self):
    #     grandchildnode = LeafNode("b","grandchild")
    #     childnode = ParentNode("span", [grandchildnode])
    #     parent_node = ParentNode("div", [childnode])
    #     self.assertEqual(parent_node.to_html(), "<div><span><b>granchild</b></span></div>")