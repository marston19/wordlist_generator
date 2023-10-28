#! /usr/bin/python3
# Keep It Simple wordlist generator.

import sys
import re

PATTERN = re.compile(r"\w{12,14}") # Hardcoded pattern for specific use in Hamlet (THM) -- Can change easily if needed.

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <filename>")

else:
    with open(sys.argv[1], 'r') as file:
        text = file.read().lower()              # Turn everything in the text to lowercase
    
    wordlist = []
    
    for word in re.findall(PATTERN, text):
        if word not in wordlist:
            wordlist.append(word)
    wordlist = sorted(wordlist)
    result = "\n".join(wordlist)
    print(result)