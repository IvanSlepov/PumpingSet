# Task 10. Stalactites or Stalagmites?
# Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.
# Create a function mineral_formation() that determines whether the input represents “stalactites” or “stalagmites”.
# If it represents both, return “both”. Input will be a 2D list, with 1 representing a piece of rock, and 0 representing air space.
# Notes.
# In other words, if the first list has 1s, return “stalactites”. If the last list has 1s, return “stalagmites”. If both have them, return “both”.
# Examples
#
# mineral_formation([
#   [0, 1, 0, 1],
#   [0, 1, 0, 1],
#   [0, 0, 0, 1],
#   [0, 0, 0, 0]
# ]) ➞ "stalactites"
# mineral_formation([
#   [0, 0, 0, 0],
#   [0, 1, 0, 1],
#   [0, 1, 1, 1],
#   [0, 1, 1, 1]
# ]) ➞ "stalagmites"
# mineral_formation([
#   [1, 0, 1, 0],
#   [1, 1, 0, 1],
#   [0, 1, 1, 1],
#   [0, 1, 1, 1]
# ]) ➞ "both"

def mineral_formation(cave_shape):
    stalactites_area = cave_shape[0]
    stalagmites_area = cave_shape[len(cave_shape) - 1]

    if max(stalactites_area) == 1 and max(stalagmites_area) == 1:
        print("both")
    elif max(stalactites_area) == 1 and max(stalagmites_area) == 0:
        print("stalactites")
    elif max(stalactites_area) == 0 and max(stalagmites_area) == 1:
        print("stalagmites")
    else:
        print("the fucking cave is empty")
