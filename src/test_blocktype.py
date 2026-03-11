import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading_one_hash(self):
        block = "# Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)


    def test_heading_six_hashes(self):
        block = "###### Heading 6"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_heading_3_hashes(self):
        block = "### Heading 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_heading_seven_hashes(self):
        block = "####### Test"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_heading_no_spaces(self):
        block = "####Test2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_valid_code_block(self):
        block = """```
Test
Test2```"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_empty_code_block(self):
        block = """```
```"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_no_end_backticks_code_block(self):
        block = """```
Test
Test2"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_quote_spaces(self):
        block = """> There is nothing to fear
> except fear itself."""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_quote_no_spaces(self):
        block = """>Yes, I'm drunk.
>But, in the morning, I'll be sober,
>and you'll still be ugly."""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_quote_mixed_spaces(self):
        block = """>Yes, I'm drunk.
> But, in the morning, I'll be sober,
> and you'll still be ugly."""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_invalid_quote(self):
        block = """>Yes, I'm drunk.
>But, in the morning, I'll be sober,
and you'll still be ugly."""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_unordered_list(self):
        block = """- ketchup
- mayonnaise
- relish"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list(self):
        block = """- ketchup
mayonnaise
- relish
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_valid_ordered_list(self):
        block = """1. ketchup
2. mustard
3. mayonnaise
4. relish
5. buns"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
    
    def test_skipped_number(self):
        block = """1. ketchup
2. mustard
3. mayonnaise
4. relish
6. buns"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_starts_at_two(self):
        block = """2. ketchup
3. mustard
4. mayonnaise
5. relish
6. buns"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_paragraph(self):
        block = "No special formatting here."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)