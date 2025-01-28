def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_char_count(text)
    print_report(book_path, num_words, character_count)

def print_report(book_path, num_words, character_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    lods = many_dicts(character_count)
    ordered = sorted(lods, key=sort_on, reverse=True)
    for i in ordered:
        for k, v in i.items():
            if k.isalpha():
                print(f"'{k}' character was found {v} times\n")

    print(f"--- End report ---")

def many_dicts(character_count):
    lod = [{k: v} for k, v in character_count.items()]
    return lod

def sort_on(d):
    v = next(iter(d.values()))
    return v

def get_char_count(text):
    char_dict = {}
    for char in text:
        l_char = char.lower()
        if l_char not in char_dict:
            char_dict[l_char] = 1
        else:
            char_dict[l_char] += 1
    return char_dict



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
