# Task 14. Sum of Prime Numbers
# Create a function sum_primes() that takes a list of numbers and returns the sum of all prime numbers in the list.
# Notes
#
# Given numbers won’t exceed 101.
# A prime number is a number which has exactly two divisors.
# Examples
#
# sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
# sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
# sum_primes([]) ➞ None


"""
THIS IMPLEMENTATION CONTAINS A BUG THAT CAN BE DISCOVERED
IF THE LIST TO CHECK CONTAINS CERTAIN NUMBERS!!!

FOR INSTANCE "22".

THE FIXED VERSION INSIDE OF THE list_manipulations.py
"""


def sum_primes(some_list):
    sum_of_prime = 0
    look_up = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    whole_division_occurrences = 0

    for entry in some_list:
        if entry == 1:
            continue
        for lookup_entry in look_up:
            division_result = entry / lookup_entry
            if division_result.is_integer():
                whole_division_occurrences += 1
        if whole_division_occurrences <= 2:
            sum_of_prime += entry
            whole_division_occurrences = 0
        else:
            whole_division_occurrences = 0

    if sum_of_prime == 0:
        return None

    return sum_of_prime
