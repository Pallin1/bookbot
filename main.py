import sys

from stats import count_words 
from stats import count_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    character_dictionary = count_characters(book_text)
    character_dictionary_list = sort_characters(character_dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in character_dictionary_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()