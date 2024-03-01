# Task 8. Nth Smallest Integer
# Given an unsorted list, create a function nth_smallest() that returns the nth smallest integer
# (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).
# Notes.
#
# n will always be >= 1.
# Each number in the array will be distinct (there will be a clear ordering).
# Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest integer, return None.
# Examples
#
# nth_smallest([1, 3, 5, 7], 1) ➞ 1
# nth_smallest([1, 3, 5, 7], 3) ➞ 5
# nth_smallest([1, 3, 5, 7], 5) ➞ None
# nth_smallest([7, 3, 5, 1], 2) ➞ 3

def nth_smallest(numbers_list, marker_number):
    if len(numbers_list) < 4:
        print("To few numbers. Please add one more.")
        return
    if marker_number >= max(numbers_list):
        print("The number you entered is too big. Try smth smaller please")
        return

    nth_smallest_number = 0
    copy_of_the_numbers_list = list(numbers_list)
    copy_of_the_numbers_list.sort()

    if marker_number < 1:
        marker_number = 1

    while len(copy_of_the_numbers_list) > 0:
        nth_smallest_number = min(copy_of_the_numbers_list)
        if nth_smallest_number <= marker_number:
            copy_of_the_numbers_list.remove(nth_smallest_number)
            continue
        elif nth_smallest_number > marker_number:
            if nth_smallest_number >= max(copy_of_the_numbers_list):
                print("None")
                break
            else:
                print(nth_smallest_number)
                break
