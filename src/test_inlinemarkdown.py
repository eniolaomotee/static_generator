from inline_markdown import (split_nodes_delimiter, extract_markdown_images, extract_markdown_links, 
                             split_nodes_images, split_nodes_links,text_to_textnodes, markdown_to_blocks)
from text_node import TextNode, TextNodeType
import unittest


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with **bolded** word",TextNodeType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**", TextNodeType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with ",TextNodeType.TEXT),
                TextNode("bolded", TextNodeType.BOLD),
                TextNode(" word", TextNodeType.TEXT)
            ],
            new_nodes
        )
    
    def test_delim_double_bold(self):
        node = TextNode("This text is **bolded** with **another**", TextNodeType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextNodeType.BOLD)
        self.assertListEqual(
            [
                TextNode("This text is ", TextNodeType.TEXT),
                TextNode("bolded",TextNodeType.BOLD),
                TextNode(" with ", TextNodeType.TEXT),
                TextNode("another", TextNodeType.BOLD)
            ],
            new_nodes
        )
        
    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextNodeType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextNodeType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNodeType.TEXT),
                TextNode("italic", TextNodeType.ITALIC),
                TextNode(" word", TextNodeType.TEXT)
            ],
            new_nodes
        )
    
    
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextNodeType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextNodeType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextNodeType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextNodeType.BOLD),
                TextNode(" and ", TextNodeType.TEXT),
                TextNode("italic", TextNodeType.ITALIC)
            ],
            new_nodes
        )
    
    
    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextNodeType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextNodeType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNodeType.TEXT),
                TextNode("code block", TextNodeType.CODE),
                TextNode(" word", TextNodeType.TEXT)
            ],new_node
        )
    

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual([("image","https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
        
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextNodeType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNodeType.TEXT),
                TextNode("image",TextNodeType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextNodeType.TEXT),
                TextNode("second image", TextNodeType.IMAGE, "https://i.imgur.com/3elNhQu.png")

            ], new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextNodeType.TEXT
        )
        new_node = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextNodeType.TEXT),
                TextNode("to boot dev",TextNodeType.LINK,"https://www.boot.dev"),
                TextNode(" and ",TextNodeType.TEXT),
                TextNode("to youtube",TextNodeType.LINK,"https://www.youtube.com/@bootdotdev")
            ],
            new_node
        )
    
    
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is ", TextNodeType.TEXT),
                TextNode("text", TextNodeType.BOLD),
                TextNode(" with an ", TextNodeType.TEXT),
                TextNode("italic", TextNodeType.ITALIC),
                TextNode(" word and a ", TextNodeType.TEXT),
                TextNode("code block", TextNodeType.CODE),
                TextNode(" and an ", TextNodeType.TEXT),
                TextNode("obi wan image", TextNodeType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextNodeType.TEXT),
                TextNode("link", TextNodeType.LINK, "https://boot.dev"),
            ],
            nodes,
        )
    
    
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
if __name__ == "__main__":
    unittest.main()
    
