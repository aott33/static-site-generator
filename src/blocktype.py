from enum import Enum
import re

class BlockType(Enum):
	PARAGRAPH = "p"
	HEADING = "h"
	QUOTE = "blockquote"
	CODE = "pre"
	UNORDERED_LIST = "ul"
	ORDERED_LIST = "ol"

def block_to_blocktype(md_block):
	block_type = BlockType.PARAGRAPH

	heading_regex = r'^\#{1,6} '
	quote_regex = r'^\>'
	code_regex = r'^\`{3}[\s\S]*\`{3}$'
	ul_regex = r'^\- '
	ol_regex = r'^\d+\.\s'

	if re.search(heading_regex, md_block):
		block_type = BlockType.HEADING
	
	elif re.search(code_regex, md_block, re.DOTALL):
		block_type = BlockType.CODE

	elif re.search(quote_regex, md_block):
		lines = md_block.split('\n')
		is_quote = True
		for line in lines:
			
			if not re.search(quote_regex, line):
				is_quote = False
				break	
		if is_quote:
			block_type = BlockType.QUOTE
	
	elif re.search(ul_regex, md_block):
		lines = md_block.split('\n')
		is_ul = True
		for line in lines:
			if not re.search(ul_regex, line):
				is_ul = False
				return block_type

		if is_ul:
			block_type = BlockType.UNORDERED_LIST
	
	elif re.search(ol_regex, md_block):
		lines = md_block.split('\n')
		is_ol = True
		expected_number = 1
		for line in lines:
			match = re.search(ol_regex, line)
			if not match or int(line[0]) != expected_number:
				is_ol = False
				return block_type

			expected_number += 1
		if is_ol:
			block_type = BlockType.ORDERED_LIST	
	
	return block_type
