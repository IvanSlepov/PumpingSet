import math


# Task 6. Probabilities
# Given a list of numbers and a value n, write a function probability() that returns the probability of choosing a number greater than or equal to n from the list.
# The probability should be expressed as a percentage, rounded to one decimal place. Notes.
# Percent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
# Examples
#
# probability([5, 1, 8, 9], 6) ➞ 50.0
# probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7
# probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0

def probability(int_list, greater_equal_number_marker):
    probability_percentage = 0.0
    number_of_list_items_greater_equal_to_marker = 0

    for entry in int_list:
        if entry >= greater_equal_number_marker:
            number_of_list_items_greater_equal_to_marker += 1

    probability_percentage = round(100 * (number_of_list_items_greater_equal_to_marker / len(int_list)), 1)

    print(probability_percentage)
