def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_wordcount(word_string):
    word_list = word_string.split()
    return len(word_list)


def get_lettercount(text):
    lowercase_text = text.lower()
    letter_counts = {}

    for ascii in range(97, 123):
        letter_counts[chr(ascii)] = 0

    for letter in lowercase_text:
        if letter in letter_counts:
            letter_counts[letter] += 1

    return letter_counts


def sort_lettercount(lettercount_dict):
    sorted_lettercount = {}
    letter_keys = list(lettercount_dict.keys())
    letter_values = list(lettercount_dict.values())

    def get_next_highest_count():
        highest_count = float("-inf")
        highest_count_index = 0
        for index in range(0, len(letter_keys)):
            if letter_values[index] >= highest_count:
                highest_count = letter_values[index]
                highest_count_index = index
        key = letter_keys.pop(highest_count_index)
        value = letter_values.pop(highest_count_index)
        sorted_lettercount[key] = value

    while len(letter_keys) > 0:
        get_next_highest_count()

    return sorted_lettercount


def main():
    book_path = "books/frakenstein.txt"
    book_text = get_book_text(book_path)
    book_wordcount = get_wordcount(book_text)
    lettercount = get_lettercount(book_text)
    sorted_lettercount = sort_lettercount(lettercount)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book_wordcount} words found in the document\n")
    for key in sorted_lettercount:
        print(f"The '{key}' character was found {sorted_lettercount[key]} times")
    print("--- End report ---")


main()
