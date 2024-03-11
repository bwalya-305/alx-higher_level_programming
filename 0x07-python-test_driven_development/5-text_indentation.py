#!/usr/bin/python3

def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ['.', '?', ':']
    for char in special_chars:
        text = text.replace(char, char + '\n\n')
    
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    
    text = '\n'.join(lines)
    print(text)

