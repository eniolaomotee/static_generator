import re

def extract_title(markdown): 
    """
    Return the text of the first H1 in the markdown (a line starting with a single '# ').
    Raise ValueError if no H1 is found.
    """
    # using a multiline search for a line that starts with exactly one '#'
    match = re.search(r'^\s*#\s+(.+?)\s*$',markdown, flags=re.MULTILINE)
    
    if not match:
        raise ValueError("No H1 heading (# ..) found in the markdown")
    return match.group(1).strip()

            
            