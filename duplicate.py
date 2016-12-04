import re
def duplicate(str):
    while re.search(r'\b(.+)(\s+\1\b)+', str):
        str = re.sub(r'\b(.+)(\s+\1\b)+', r'\1', str)
    return(str)
