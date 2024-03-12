# Task 1. Is the Word Singular or Plural?
# Create a function is_plural() that takes in a word and determines whether or not it is plural. A plural word is one that ends in “s”.
# Notes. This is an oversimplification of the English language. We are ignoring edge cases like “goose” and “geese”, “fungus” and “fungi”, etc.
# Examples
#
# is_plural("changes") ➞ True
# is_plural("change") ➞ False
# is_plural("dudes") ➞ True
# is_plural("magic") ➞ False

def is_plural(word: str) -> bool:
    is_plural_word = False

    plural_ending = "s"

    if word[len(word) - 1] == plural_ending:
        is_plural_word = True
        return is_plural_word
    else:
        is_plural_word = False
        return is_plural_word
