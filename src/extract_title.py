import re

def extract_title(markdown):
    pattern = r'\#\s+(.+)'
    match = re.search(pattern, markdown)

    if match:
        return match.group().split('# ', 1)[1].strip()
    else:
        raise Exception('File does not have header')
