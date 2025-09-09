
def markdown_to_blocks(markdown):
    rawoutput = markdown.split("\n\n")
    filtered_output = []
    for block in rawoutput:
        if not block.strip():
            continue
        cleaned = [line.strip() for line in block.splitlines() if line.strip()]
        if cleaned:
            filtered_output.append("\n".join(cleaned))
    return filtered_output