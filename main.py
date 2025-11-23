from stats import count_words
from stats import count_characters
from stats import print_report
import sys

def get_book_text(path):
    with open(path) as f:
        path_text = f.read()
        return path_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    wordcount = count_words(get_book_text(sys.argv[1]))
    total_characters = count_characters(get_book_text(sys.argv[1]))


    title_str = f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {wordcount} total words\n--------- Character Count -------"
    footer_str = f"============= END ==============="
    print(title_str)
    print_report(total_characters)
    print(footer_str)

    
main()