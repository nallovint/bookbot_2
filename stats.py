def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict:
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

