from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def is_heading(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break

    if count == 0 or count > 6:
        return False

    if count >= len(block):
        return False

    if block[count] != " ":
        return False
    text = block[count + 1:]
    if not text:
        return False
    
    return True


def is_code(block):
    if not block.startswith("```\n") or not block.endswith("```"):
        return False
    
    if not block[4:-3]:
        return False
    
    return True

def is_quote(block):    
    for line in block.split("\n"):
        if not line.startswith(">"):
            return False
    return True

def is_unordered_list(block):
    for line in block.split("\n"):
        if not line.startswith("- "):
            return False
    return True

def is_ordered_list(block):
    lines = block.split("\n")
    for i, line in enumerate(lines, start=1):
        expected_prefix = f"{i}. "
        if not line.startswith(expected_prefix):
            return False
    return True


def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    elif is_code(block):
        return BlockType.CODE
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH