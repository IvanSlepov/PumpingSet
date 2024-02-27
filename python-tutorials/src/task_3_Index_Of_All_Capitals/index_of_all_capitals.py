# Task 3. Return the Index of All Capital Letters
# Create a function index_of_caps() that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
# Notes.
#
# Return an empty list if no uppercase letters are found in the string.
# Special characters ($#@%) and numbers will be included in some test cases.
# Assume all words do not have duplicate letters.
# Examples
#
# index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
# index_of_caps("determine") ➞ []
# index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
# index_of_caps("sUn") ➞ [1]

def index_of_caps(word):

    if not isinstance(word, str):
        print("The argument is not a string!!!")
        return

    capital_list = []

    for letter in word:
        is_upper_letter = letter.isupper()
        if is_upper_letter:
            capital_list.append(letter)

    print(capital_list)
