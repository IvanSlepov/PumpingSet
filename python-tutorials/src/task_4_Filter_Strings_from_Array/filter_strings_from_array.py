# Task 4. Filter Strings from Array
# Create a function filter_list() that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
# Examples
#
# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
# filter_list(["Nothing", "here"]) ➞ []

def filter_list(list_to_check):

    int_list = []

    for entry in list_to_check:
        if isinstance(entry, int):
            int_list.append(entry)

    print(int_list)

test_list = [1, 2, "g", 5, "TT"]

filter_list(test_list)