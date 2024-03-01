# Task 13. Tallest Skyscraper
# A city skyline can be represented as a 2-D list with 1s representing buildings.
# In the example below, the height of the tallest building is 4 (second-most right column).
#
# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]
# Create a function tallest_skyscraper() that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
# Examples
#
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 3
# tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 4
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [1, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 2


def tallest_skyscraper(skyline_two_d_list):

    level_reached = 0

    for level in skyline_two_d_list:
        if max(level) == 1:
            level_reached += 1

    return level_reached
