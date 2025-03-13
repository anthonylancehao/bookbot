
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_count(path):
    text = get_book_text(path)
    return len(text.split())


def count_characters(path):
    text = get_book_text(path)
    char_count = {}
    text = text.lower()  # Convert to lowercase

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1  # Use .get() for cleaner code

    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    return sorted_char_count
