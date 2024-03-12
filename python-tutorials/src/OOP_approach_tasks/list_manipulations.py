from typing import Self


# The ListManipulations class implements the methods
# from tasks: 4, 6-8, and 10-15, inclusive


class ListManipulations:
    def __init__(self, list_to_process: list):
        self.list_to_process: list = list_to_process

    def filter_list(self, my_list: list = None) -> list:
        """
        The 'filter_list' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method. It parses the given list and
        returns the new list containing integers if any, or returns the
        original list otherwise.

        :param my_list: expecting a random list
        :return filter_list_to_process: the new list containing integers if any, or returns the
        original list otherwise
        """
        filter_list_to_process: list = my_list if my_list else self.list_to_process

        int_list: list = []

        for entry in filter_list_to_process:
            if isinstance(entry, int):
                int_list.append(entry)

        if len(int_list) > 0:
            return int_list
        else:
            return filter_list_to_process

    def probability(self, greater_equal_number_marker: int, my_list: list = None) -> float:
        """
        The 'probability' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method.
        It returns the probability of choosing a number
        greater than or equal to the given number, from the list.

        :param greater_equal_number_marker: a number that will be used
        as a marker for probability
        :param my_list: expecting a list with random ints
        :return probability_percentage: the probability of choosing a number
        greater than or equal to the given number, from the list
        """
        probability_list_to_process: list = my_list if my_list else self.list_to_process

        probability_percentage: float = 0.0
        number_of_list_items_greater_equal_to_marker: int = 0

        for entry in probability_list_to_process:
            if entry >= greater_equal_number_marker:
                number_of_list_items_greater_equal_to_marker += 1

        probability_percentage = (
            round(100 * (number_of_list_items_greater_equal_to_marker / len(probability_list_to_process)), 1)
        )

        return probability_percentage

    def chatroom_status(self, my_list: list = None) -> str:
        """
        The 'chatroom_status' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method. It returns the number of users in a chatroom based on the following rules:

        # If there is no one, return “no one online”.
        # If there is 1 person, return “user1 online”.
        # If there are 2 people, return user1 and user2 online”.
        # If there are n>2 people, return the first two names and add “and n-2 more online”.
        # For example, if there are 5 users, return: "user1, user2 and 3 more online"

        :param my_list: expecting a list with random names
        :return chatroom_status_str: returns the number of users in a chatroom
        on the shape of str
        """
        chatroom_list_to_process: list = my_list if my_list else self.list_to_process

        number_of_users_in_the_list: int = len(chatroom_list_to_process)
        chatroom_status_str: str

        if number_of_users_in_the_list == 0:
            chatroom_status_str = "No one online."
            return chatroom_status_str
        if number_of_users_in_the_list == 1:
            chatroom_status_str = f"{chatroom_list_to_process[0]} is online."
            return chatroom_status_str
        if number_of_users_in_the_list == 2:
            chatroom_status_str = f"{chatroom_list_to_process[0]} and {chatroom_list_to_process[1]} are online."
            return chatroom_status_str
        if number_of_users_in_the_list > 2:
            chatroom_status_str = (f"{chatroom_list_to_process[0]}, {chatroom_list_to_process[1]} and "
                                   f"{len(chatroom_list_to_process) - 2} more are online.")
            return chatroom_status_str

    def nth_smallest(self, marker_int: int, my_list: list = None) -> int:
        """
        The 'nth_smallest' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method. It returns the nth smallest integer
        # (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).
        # Notes.
        #
        # n will always be >= 1.
        # Each number in the array will be distinct (there will be a clear ordering).
        # Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest integer,
        return None.

        :param marker_int: expecting an int that'll be used a starting point
        to search for the next smallest int in the list
        :param my_list: expecting a list with random integers
        :return nth_smallest_number: the nth smallest integer
        """
        smallest_list_to_process: list = my_list if my_list else self.list_to_process
        nth_smallest_number: int = 0

        if len(smallest_list_to_process) < 4:
            print("To few numbers. Please add one more.")
            return nth_smallest_number
        if marker_int >= max(smallest_list_to_process):
            print("The number you entered is too big. Try smth smaller please")
            return nth_smallest_number

        nth_smallest_number: int = 0
        copy_of_the_numbers_list: list = list(smallest_list_to_process)
        copy_of_the_numbers_list.sort()

        if marker_int < 1:
            marker_int = 1

        while len(copy_of_the_numbers_list) > 0:
            nth_smallest_number = min(copy_of_the_numbers_list)
            if nth_smallest_number <= marker_int:
                copy_of_the_numbers_list.remove(nth_smallest_number)
                continue
            elif nth_smallest_number > marker_int:
                if nth_smallest_number >= max(copy_of_the_numbers_list):
                    nth_smallest_number = None
                    return nth_smallest_number
                else:
                    return nth_smallest_number

    def mineral_formation(self, my_list: list = None) -> str:
        """
        The 'mineral_formation' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method. It determines whether the input represents “stalactites” or “stalagmites”.
        # If it represents both, return “both”. Input will be a 2D list, with 1 representing a piece of rock,
        # and 0 representing air space.
        # Notes.
        # In other words, if the first list has 1s, return “stalactites”. If the last list has 1s, return “stalagmites”.
        # If both have them, return “both”.

        :param my_list: expecting a 2D list with 0 and 1
        :return minerals: str with info about a cave
        """
        mineral_formation_list_to_process: list = my_list if my_list else self.list_to_process

        stalactites_area: list = mineral_formation_list_to_process[0]
        stalagmites_area: list = mineral_formation_list_to_process[len(mineral_formation_list_to_process) - 1]

        minerals: str

        if max(stalactites_area) == 1 and max(stalagmites_area) == 1:
            minerals = "Both"
            return minerals
        elif max(stalactites_area) == 1 and max(stalagmites_area) == 0:
            minerals = "Stalactites"
            return minerals
        elif max(stalactites_area) == 0 and max(stalagmites_area) == 1:
            minerals = "Stalagmites"
            return minerals
        else:
            minerals = "The fucking cave is empty."
            return minerals

    def pops(self, my_list: list = None) -> list:
        """
        The 'pops' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method.

        Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.
        # The effect of a water balloon popping can be modeled using a list.
        # Create a function pops() that takes a list which takes the pre-pop state and returns the state after the balloon is popped.
        # The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element. Notes.
        #
        # Length of input list is always odd.
        # The input list will always be the exact length it takes for there to be exactly one border zero.
        # If the input list consists only of zeroes, return the same list.

        :param my_list: expecting a list
        :return wet_zone: returns a list
        """
        pops_list_to_process: list = my_list if my_list else self.list_to_process

        wet_zone: list = list(pops_list_to_process)
        wet_zone.remove(max(wet_zone))

        if len(pops_list_to_process) % 2 == 0:
            print("Please add or remove 1 entry to make list length odd.")
            return pops_list_to_process
        elif pops_list_to_process[0] != 0 or pops_list_to_process[len(pops_list_to_process) - 1] != 0:
            print("Please make the first and/or last element 0/es.")
            return pops_list_to_process
        elif max(pops_list_to_process) == 0:
            return pops_list_to_process
        elif len(pops_list_to_process) - (max(pops_list_to_process) * 2 - 1) < 2:
            print("Please decrease the entry in your list.")
            return pops_list_to_process
        elif max(wet_zone) > 0:
            print("Please make sure there's only one entry grater than 0.")
            return pops_list_to_process
        elif pops_list_to_process.index(max(pops_list_to_process)) != ((len(pops_list_to_process) - 1) / 2):
            print("Please move your entry to the middle of the list.")
            return pops_list_to_process
        else:
            wet_zone = list(pops_list_to_process)
            balloon_power: int = max(wet_zone)
            index_of_balloon_incr: int = wet_zone.index(max(wet_zone))
            index_of_balloon_decr: int = wet_zone.index(max(wet_zone))

            while balloon_power > 1:
                balloon_power -= 1
                wet_zone[index_of_balloon_decr - 1] = balloon_power
                wet_zone[index_of_balloon_incr + 1] = balloon_power
                index_of_balloon_incr += 1
                index_of_balloon_decr -= 1

            return wet_zone

    def count_overlapping(self, number_to_search: int, my_list: list = None) -> int:
        """
        The 'count_overlapping' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method.

        It takes in a list of intervals
        and returns how many intervals overlap with a given point.
        An interval overlaps a particular point if the point exists inside the interval, or on the interval’s boundary.

        For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary)

        :param number_to_search: int that will be searched in the 2D list
        :param my_list: expecting a 2D list with integers
        :return overlap_counter: int of how many intervals overlap with a 'number_to_search'
        """
        count_overlapping_list_to_process: list = my_list if my_list else self.list_to_process

        overlap_counter: int = 0

        for first_d in count_overlapping_list_to_process:
            if first_d[0] <= number_to_search <= first_d[len(first_d) - 1]:
                overlap_counter += 1
                continue
            for second_d in first_d:
                if second_d == number_to_search:
                    overlap_counter += 1

        return overlap_counter

    def tallest_skyscraper(self, my_list: list = None) -> int:
        """
        The 'tallest_skyscraper' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method.

        It takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper,
        which is determined by presence of number 1 in each list.

        :param my_list: expecting a 2D list with 0 and 1
        :return level_reached: the height(int) of the tallest skyscraper
        """
        skyscraper_list_to_process: list = my_list if my_list else self.list_to_process
        level_reached: int = 0

        for level in skyscraper_list_to_process:
            if max(level) == 1:
                level_reached += 1

        return level_reached

    def sum_primes(self, my_list: list = None) -> int:
        """
        The 'sum_primes' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method.

        It takes a list of numbers and returns the sum of all prime numbers in the list.

        :param my_list: expecting a list with random ints
        :return sum_of_prime: the sum of all prime numbers in the list
        """
        primes_list_to_process: list = my_list if my_list else self.list_to_process

        sum_of_prime: int = 0
        look_up: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        whole_division_occurrences: int = 0

        for entry in primes_list_to_process:
            if entry == 1:
                continue
            else:
                look_up.append(entry) if entry > 9 else look_up
                for lookup_entry in look_up:
                    division_result = entry / lookup_entry
                    if division_result.is_integer():
                        whole_division_occurrences += 1
                look_up.remove(entry) if entry > 9 else look_up
                if whole_division_occurrences <= 2:
                    sum_of_prime += entry
                    whole_division_occurrences = 0
                else:
                    whole_division_occurrences = 0

        if sum_of_prime == 0:
            return sum_of_prime

        return sum_of_prime

    def show_the_love(self, my_list: list = None) -> list:
        """
        The 'show_the_love' method processes either a list set
        while constructing the object of the StringManipulation class
        or passed directly to the method.

        It removes 25% from every number in the list
        except the smallest number, and adds the total amount removed to the smallest number.

        :param my_list: expecting a list with random numbers
        :return love_list_to_process: the total amount removed to the smallest number
        """
        love_list_to_process: list = my_list if my_list else self.list_to_process

        copy_of_some_list: list = list(love_list_to_process)

        if len(love_list_to_process) < 2:
            print("Too few numbers in the list. Please make sure there are at least 2 of them.")
            return love_list_to_process

        min_int: int = min(love_list_to_process)
        copy_of_some_list.remove(min_int)

        if min(copy_of_some_list) == min_int:
            print("Please remove or change duplicate min values.")
            return love_list_to_process

        add_to_min: int = 0
        stable_min_index: int = love_list_to_process.index(min(love_list_to_process))

        for entry in love_list_to_process:
            if entry == min(love_list_to_process):
                continue
            else:
                add_to_min += entry / 4
                entry_index = love_list_to_process.index(entry)
                love_list_to_process[entry_index] -= entry / 4

        love_list_to_process[stable_min_index] += add_to_min

        return love_list_to_process
