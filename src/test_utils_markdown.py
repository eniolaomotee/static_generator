import unittest
from utils_markdown import extract_title
class TestExtractTitle(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        
    def test_stripping(self):
        md = "   #   Hello World   \nSome other line"
        self.assertEqual(extract_title(md), "Hello World")
        
    def test_later_line(self):
        md = "Intro text\n\n# The Title\nMore"
        self.assertEqual(extract_title(md), "The Title")

    def test_no_h1_raises(self):
        with self.assertRaises(ValueError):
            extract_title("## Not H1\nNo h1 here")


    
if __name__ == "__main__":
    unittest.main()