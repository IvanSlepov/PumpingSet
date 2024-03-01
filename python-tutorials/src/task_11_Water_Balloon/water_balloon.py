# Task 11. Water Balloon
# Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.
# The effect of a water balloon popping can be modeled using a list.
# Create a function pops() that takes a list which takes the pre-pop state and returns the state after the balloon is popped.
# The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element. Notes.
#
# Length of input list is always odd.
# The input list will always be the exact length it takes for there to be exactly one border zero.
# If the input list consists only of zeroes, return the same list.
# Examples
#
# pops([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
# pops([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
# pops([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
# pops([0]) ➞ [0]

def pops(danger_zone):
    wet_zone = list(danger_zone)
    wet_zone.remove(max(wet_zone))

    if len(danger_zone) % 2 == 0:
        print("Please add or remove 1 entry to make list length odd")
        return
    elif danger_zone[0] != 0 or danger_zone[len(danger_zone) - 1] != 0:
        print("Please make the first and/or last element 0/es")
        return
    elif max(danger_zone) == 0:
        print(danger_zone)
        return
    elif len(danger_zone) - (max(danger_zone) * 2 - 1) < 2:
        print("Please decrease the entry in your list")
        return
    elif max(wet_zone) > 0:
        print("Please make sure there's only one entry grater than 0")
        return
    elif danger_zone.index(max(danger_zone)) != ((len(danger_zone) - 1) / 2):
        print("Please move your entry to the middle of the list")
        return
    else:
        wet_zone = list(danger_zone)
        balloon_power = max(wet_zone)
        index_of_balloon_incr = wet_zone.index(max(wet_zone))
        index_of_balloon_decr = wet_zone.index(max(wet_zone))

        while balloon_power > 1:
            balloon_power -= 1
            wet_zone[index_of_balloon_decr - 1] = balloon_power
            wet_zone[index_of_balloon_incr + 1] = balloon_power
            index_of_balloon_incr += 1
            index_of_balloon_decr -= 1

        print(wet_zone)
