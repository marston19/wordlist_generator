#! /usr/bin/python3
# wordlist_generator.py
# Create a wordlist from all -UNIQUE- words in a text file. Supports RegEx to define what kind of words to grab.

import os
import re
import argparse

PATTERN = re.compile(r"\w{4,}") # Basic pattern, gathers words from 4 letters on.

def wordlist_generator(arguments):
    """Wordlist generator that does the heavy lifting. 
    Open the file, apply either the basic or custom regex, write an output file or print to screen."""
    with open(arguments.filename) as file:
        text = file.read().lower()

    if arguments.regex:
        result = use_custom_regex(text, arguments.regex)
    else:
        result = sort_and_unique(re.findall(PATTERN, text))

    final_result = "\n".join(result)
    
    if arguments.output:
        write_output(final_result, arguments.output)
    else:
        print(final_result)
   

def write_output(generated_wordlist: list|str, filename: str):
    """Simple function to write the script output to the specified filename."""
    print(f"Saving wordlist as {filename}")
    with open(filename, 'w') as saved_file:
        saved_file.write(generated_wordlist)

def use_custom_regex(text: list|str, regex: str):
    """If a custom regex is passed to the script, compile, find, sort and unique-fy based on it."""
    pattern = re.compile(fr"{regex}")
    re_result = sort_and_unique(re.findall(pattern, text))
    return re_result

def sort_and_unique(result: list):
    """Take the input text or list, sort it and make it only unique entries."""
    wordlist = []
    for word in result:
        if word not in wordlist:
            wordlist.append(word)
    wordlist = sorted(wordlist)
    return wordlist

def main():
    parser = argparse.ArgumentParser(
        description="Create a wordlist from all unique words in text file.",
    )
    parser.add_argument("filename")
    parser.add_argument("-r", "--regex", help="Filter words based on RegEx", action="store")
    parser.add_argument("-o", "--output", help="Save output to file.", action="store")

    args = parser.parse_args()

    try:
        wordlist_generator(args)
    except FileNotFoundError as e:
        print(e)
 
if __name__ == "__main__":
    main()