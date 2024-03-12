from typing import Self
from datetime import datetime


# The following class implements the tasks 1-3, 5 and 9
# using the OOP approach

class StringManipulation:
    def __init__(self, word_to_process: str):
        self.word_to_process: str = word_to_process

    def __repr__(self):
        string_manipulation_description: str = f"StringManipulation: {self.word_to_process}"
        return string_manipulation_description

    def is_plural(self, word: str = None) -> bool:
        """
        The 'is_plural' method processes either a word set
        while constructing the object of the StringManipulation class
        or passed directly to the method. It returns True if the passed
        word has an 's' ending or False if it does not.

        :param word: expecting a string that has/hasn't the 's', 'es' ending
        :return is_plural_word: returns 'true' if passed word has 's', 'es' ending
        and 'false' otherwise
        """
        is_plural_word_to_process: str = word if word else self.word_to_process

        is_plural_word: bool = False
        plural_ending: str = "s"

        if is_plural_word_to_process[len(is_plural_word_to_process) - 1] == plural_ending:
            is_plural_word = True
            return is_plural_word
        else:
            is_plural_word = False
            return is_plural_word

    def stutter(self, word: str = None) -> str:
        """
        The 'stutter' method processes either a word set
        while constructing the object of the StringManipulation class
        or passed directly to the method.
        It returns the stutter version of
        the original word.

        :param word: expecting a random string
        :return final_stutter: the stutter version of the original word.
        """
        stutter_word_to_process: str = word if word else self.word_to_process

        i: int = 0
        stutter_part: str = stutter_word_to_process[0:2]
        final_stutter: str = ""

        while i < 3:
            final_stutter += stutter_part + "... "
            i += 1
            if i == 2:
                final_stutter += stutter_word_to_process + "?"
                break

        return final_stutter

    def index_of_caps(self, word: str = None) -> dict:
        """
        The 'index_of_caps' method processes either a word set
        while constructing the object of the StringManipulation class
        or passed directly to the method. It returns a dictionary with indexes
        of the capital letters(if any) in the given word or an empty dict otherwise.

        :param word: expecting a random string
        :return capital_dict: a dictionary with indexes
        of the capital letters(if any) in the given word or an empty dict otherwise.
        """
        capital_dict: dict = {}
        index_of_cap_letter: int
        index_of_caps_word_to_process: str = word if word else self.word_to_process

        if not isinstance(index_of_caps_word_to_process, str):
            print("The argument is not a string!!!")
            return capital_dict

        for letter in index_of_caps_word_to_process:
            is_upper_letter = letter.isupper()
            if is_upper_letter:
                capital_dict[letter] = index_of_caps_word_to_process.index(letter)
        return capital_dict

    @staticmethod
    def remove_char_from_str(str_to_process: str, char_to_remove: str, char_to_replace_removed: str) -> str:
        """
        The 'remove_char_from_str' method replaces the given char in a string.
        It returns the replaced char str.

        :param str_to_process: expecting a random string
        :param char_to_remove: expecting a char that should be removed from 'str_to_process'
        :param char_to_replace_removed: expecting a char that should replace the removed one
        :return str_to_process: returns a modified string
        """
        if str_to_process.find(char_to_remove) != -1:
            print(f"Replaced '{char_to_remove}' in '{str_to_process}' with '{char_to_replace_removed}'")
            str_to_process = str_to_process.replace(char_to_remove, char_to_replace_removed)
            return str_to_process
        else:
            print(f"Did not find any '{char_to_remove}' char in '{str_to_process}'.")
            return str_to_process

    def alphabet_soup(self, word: str = None) -> str:
        """
        The 'alphabet_soup' method processes either a word set
        while constructing the object of the StringManipulation class
        or passed directly to the method. It returns the string with the
        letters of the original word argument ordered by their appearance
        in the English alphabet.

        :param word: expecting a random string
        :return filtered_word: the string with the
        letters of the original word argument ordered by their appearance
        in the English alphabet
        """
        alphabet_soup_word: str = word if word else self.word_to_process

        if not isinstance(alphabet_soup_word, str):
            print("That's not a string!")
            alphabet_soup_word = "None"
            return alphabet_soup_word

        print("Initial word: " + alphabet_soup_word)

        alphabet_soup_word = self.remove_char_from_str(alphabet_soup_word, " ", "")

        lookup: str = "abcdefghijklmnopqrstuvwxyz"

        alphabet_soup_word_lower: str = alphabet_soup_word.lower()
        filtered_word: str = ""
        sorted_letter: str = ""
        lookup_entry_index: int = 0
        word_letter_indexes: list = []

        for entry in alphabet_soup_word_lower:
            lookup_entry_index = lookup.index(entry)
            word_letter_indexes.append(lookup_entry_index)

        while len(word_letter_indexes) > 0:
            sorted_letter_index = min(word_letter_indexes)
            sorted_letter = lookup[sorted_letter_index]
            filtered_word += sorted_letter
            word_letter_indexes.remove(sorted_letter_index)

        filtered_word = "Filtered by index of the letter in alphabet word: " + filtered_word
        return filtered_word

    @classmethod
    def format_date(cls, date_to_format: str) -> Self:
        """
        The 'format_date' method processes a date passed to the
        StringManipulation class additional constructor
        It returns the formatted to YYYY-DD-MM datetype string.

        :param date_to_format: expecting a date MM/DD/YYYY format string
        :return word_to_process: the formatted to YYYY-DD-MM datetype string
        """
        split_date = date_to_format.split("/")

        month = int(split_date[0])
        day = int(split_date[1])
        year = int(split_date[2])

        required_date_format = datetime(year, month, day)
        word_to_process: str = required_date_format.strftime("%Y-%d-%m")
        return cls(word_to_process)
