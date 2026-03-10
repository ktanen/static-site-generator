def markdown_to_blocks(markdown):
    blocks = []

    potential_blocks = markdown.split("\n\n")
    
    for block in potential_blocks:
        block = block.strip()
        if block:
            blocks.append(block)
        


    return blocks