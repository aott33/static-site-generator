import unittest
from blocktype import block_to_blocktype, BlockType

class TestBlockToBlockType(unittest.TestCase):
	
	def test_paragraph(self):
		text = '''This is a regular paragraph with some text.
It can have multiple lines but doesn't match any special formatting.
Just plain text content.'''
		correct_type = BlockType.PARAGRAPH
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_heading_h1(self):
		text = '''# This is a heading'''
		correct_type = BlockType.HEADING
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_heading_h6(self):
		text = '''###### This is an h6 heading'''
		correct_type = BlockType.HEADING
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_code_block(self):
		text = '''```
def hello_world():
	print("Hello, world!")
	return True
```'''
		correct_type = BlockType.CODE
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_code_block_single_line(self):
		text = '''```print("hello")```'''
		correct_type = BlockType.CODE
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_quote(self):
		text = '''> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.'''
		correct_type = BlockType.QUOTE
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_quote_single_line(self):
		text = '''> This is a single line quote'''
		correct_type = BlockType.QUOTE
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_unordered_list(self):
		text = '''- First item in the list
- Second item in the list
- Third item with more text
- Fourth and final item'''
		correct_type = BlockType.UNORDERED_LIST
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_unordered_list_single_item(self):
		text = '''- Single list item'''
		correct_type = BlockType.UNORDERED_LIST
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_ordered_list(self):
		text = '''1. First item in ordered list
2. Second item in ordered list
3. Third item in ordered list
4. Fourth item in ordered list'''
		correct_type = BlockType.ORDERED_LIST
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_ordered_list_single_item(self):
		text = '''1. Single ordered list item'''
		correct_type = BlockType.ORDERED_LIST
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_invalid_ordered_list_wrong_numbers(self):
		text = '''1. First item
3. Third item (skipped 2)
4. Fourth item'''
		correct_type = BlockType.PARAGRAPH
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_invalid_ordered_list_wrong_start(self):
		text = '''2. Starting at 2 instead of 1
3. Second item
4. Third item'''
		correct_type = BlockType.PARAGRAPH
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_mixed_content_not_quote(self):
		text = '''> This starts as a quote
But this line doesn't have a > symbol
> So it should not be a quote block'''
		correct_type = BlockType.PARAGRAPH
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)
	
	def test_mixed_content_not_unordered_list(self):
		text = '''- This starts as a list
But this line doesn't have a dash
- So it should not be a list block'''
		correct_type = BlockType.PARAGRAPH
		analyzed_type = block_to_blocktype(text)
		self.assertEqual(
			correct_type,
			analyzed_type,
		)

if __name__ == "__main__":
	unittest.main()
