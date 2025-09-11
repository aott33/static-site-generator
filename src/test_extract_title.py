import unittest
from extract_title import extract_title

class ExtractTitle(unittest.TestCase):
    def test_no_header(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here
     
    This is another paragraph with _italic_ text and `code` here

    """
        with self.assertRaises(Exception):
            result = extract_title(md)

    def test_with_header(self):
        md = """
    # Header 1
    This is **bolded** paragraph
    text in a p
    tag here
     
    This is another paragraph with _italic_ text and `code` here

    """
        result = extract_title(md)
        self.assertEqual(result, 'Header 1')
