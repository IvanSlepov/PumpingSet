# Task 15. Sharing is Caring
# Given a list of numbers, create a function show_the_love() that removes 25% from every number in the list
# except the smallest number, and adds the total amount removed to the smallest number.
# Notes

# There will only be one smallest number in a given list.
# Examples

# show_the_love([4, 1, 4]) ➞ [3, 3, 3]
# show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
# show_the_love([2, 100]) ➞ [27, 75]

def show_the_love(some_list):
    copy_of_some_list = list(some_list)

    if len(some_list) < 2:
        print("Too few numbers in the list. Please make sure there are at least 2 of them")
        return

    x = min(some_list)
    copy_of_some_list.remove(x)

    if min(copy_of_some_list) == x:
        print("Please remove or change duplicate min values")
        return

    add_to_min = 0
    stable_min_index = some_list.index(min(some_list))

    for entry in some_list:
        if entry == min(some_list):
            continue
        else:
            add_to_min += entry / 4
            entry_index = some_list.index(entry)
            some_list[entry_index] -= entry / 4

    some_list[stable_min_index] += add_to_min

    print(some_list)
