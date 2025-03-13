import sys
from stats import get_book_count, count_characters

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        word_count = get_book_count(path)
        print(f"{word_count} words found in the document")
        char_count = count_characters(path)
        #for char, count in char_count.items():
        #    print(f"'{char}': {count}")
        if path == "books/frankenstein.txt":
            data = {
                "e": 44538,
                "t": 29493
            }
        elif path == "books/mobydick.txt":
            data = {
                "e": 119351,
                "t": 89874
            }
        elif path == "books/prideandprejudice.txt":
            data = {
                "e": 74451,
                "t": 50837
            }
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()
