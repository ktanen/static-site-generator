import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        markdown = "# Testing\nExtraction"
        title = extract_title(markdown)
        self.assertEqual(title, "Testing")
    
    def test_multiple_heading_levels(self):
        markdown = "## Testing\n### Multiple\n# Extraction Levels"
        title = extract_title(markdown)
        self.assertEqual(title, "Extraction Levels")
    
    def test_leading_trailing_spaces(self):
        markdown = "#   Hello    "
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")
    
    def test_no_h1_heading(self):
        markdown = "### Hello"
        with self.assertRaises(Exception):
            title = extract_title(markdown)
        
if __name__ == "__main__":
    unittest.main()