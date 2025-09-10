from markdown_to_blocks import markdown_to_blocks, block_to_block, BlockType,markdown_to_html
import unittest

class TestMarkdownBlock(unittest.TestCase):
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
        
    def test_block_to_heading(self):
        block = "# heading"
        self.assertEqual(block_to_block(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block(block), BlockType.PARAGRAPH)

    
    def test_paragraph(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            """

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_lists(self):
        md = """
            - This is a list
            - with items
            - and _more_ items

            1. This is an `ordered` list
            2. with items
            3. and more items

            """
        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
    def test_blockquote(self):
        md = """
            > This is a
            > blockquote block

            this is paragraph text

            """

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
    
    def test_code(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
if __name__ == "__main__":
    unittest.main()