# Task 5. Alphabet Soup
# Create a function alphabet_soup() that takes a string and returns a string with its letters in alphabetical order. Notes.
# You can assume numbers and punctuation symbols won’t be included in test cases. You’ll only have to deal with single word, alphabetic characters.
# Examples
#
# alphabet_soup("hello") ➞ "ehllo"
# alphabet_soup("hacker") ➞ "acehkr"
# alphabet_soup("geek") ➞ "eegk"
# alphabet_soup("javascript") ➞ "aacijprstv"

lookup = "abcdefghijklmnopqrstuvwxyz"

def alphabet_soup(word):

    if not isinstance(word, str):
        print("That's not a string!")
        return

    print("Initial word: " + word)

    word = word.lower()

    filtered_word = ""
    sorted_letter = ""
    lookup_entry_index = 0
    word_letter_indexes = []

    for entry in word:
        lookup_entry_index = lookup.index(entry)
        word_letter_indexes.append(lookup_entry_index)

    while len(word_letter_indexes) > 0:
        sorted_letter_index = min(word_letter_indexes)
        sorted_letter = lookup[sorted_letter_index]
        filtered_word += sorted_letter
        word_letter_indexes.remove(sorted_letter_index)

    print("Filtered by index of the letter in alphabet word: " + filtered_word)

alphabet_soup("JAVASCRIPT")