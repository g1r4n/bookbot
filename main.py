from stats import get_book_text
from stats import get_char_count
from stats import get_dict_array
from stats import report
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    #path = "books/frankenstein.txt"
    path = sys.argv[1]
    content = get_book_text(f"./{path}")
    num = count(content)
    dict = get_char_count(content)
    dict_array = get_dict_array(dict)
    report(path, num, dict_array)

def count(content):
    return len(content.split())

main()
