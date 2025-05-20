from stats import count_words, count_characters
import datetime
import sys

def get_book_text(filepath):
    with open(filepath, "r") as f:
        book_text = f.read()
        return book_text

def main():
    if len(sys.argv) != 2:
        # Usage: python3 main.py <path_to_book>
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {filepath}...
    ----------- Word Count ----------
    Found {count_words(book_text)} total words
    --------- Character Count -------""")

    char_counts = count_characters(book_text)
    # Sort characters by count in descending order
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f'{char}: {count}')

if __name__ == "__main__":
    main()
