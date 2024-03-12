from task_1_Word_Singular_or_Plural import is_word_singular_or_plural
from task_2_Stuttering_Function import stuttering_function
from task_3_Index_Of_All_Capitals import index_of_all_capitals
from task_4_Filter_Strings_from_Array import filter_strings_from_array
from task_5_Alphabet_Soup import alphabet_soup
from task_6_Probabilities import probabilities
from task_7_Chat_Room_Status import chat_room_status
from task_8_Nth_Smallest_Integer import nth_smallest_integer
from task_9_Date_Format import date_format
from task_10_Stalactites_Or_Stalagmites import stalactites_or_stalagmites
from task_11_Water_Balloon import water_balloon
from task_12_Intersecting_Intervals import intersecting_intervals
from task_13_Tallest_Skyscraper import tallest_skyscraper
from task_14_Sum_Of_Prime_Numbers import sum_of_prime_numbers
from task_15_Sharing_Is_Caring import sharing_is_caring
from OOP_approach_tasks.string_manipulations import StringManipulation
from OOP_approach_tasks.list_manipulations import ListManipulations


some_list = [7, 4, 17, 14, 12, 3]
min_form_list = [[0, 0, 0, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0]]
for_pops_list = [0, 0, 0, 0, 2, 0, 0, 0, 0]
for_count_overlapping = [[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]]
for_skyscraper = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]
for_prime_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                     11, 12, 13, 14, 15, 16, 17, 18,
                     19, 20, 21, 22, 23, 24, 25, 26,
                     27, 28, 29, 30, 31, 32, 33, 34,
                     35, 36, 37, 38, 39, 40, 41, 42,
                     43, 44, 45, 46, 47, 48, 49, 50,
                     51, 52, 53, 54, 55, 56, 57, 58,
                     59, 60, 61, 62, 63, 64, 65, 66,
                     67, 68, 69, 70, 71, 72, 73, 74,
                     75, 76, 77, 78, 79, 80, 81, 82,
                     83, 84, 85, 86, 87, 88, 89, 90,
                     91, 92, 93, 94, 95, 96, 97, 98,
                     99, 100]
for_prime_numbers_2 = [2, 3, 4, 11, 20, 50, 71]
for_love = [4, 1, 4]

str_manipulator = StringManipulation("gee")
list_manipulator = ListManipulations(some_list)

if __name__ == '__main__':
    # print("hello, main.py")
    # print(str_manipulator.stutter())
    # print(str_manipulator.is_plural("horses"))
    # print(str_manipulator.alphabet_soup("damn it"))
    # print(StringManipulation.remove_char_from_str
    #       ("Nice shorts babe.", " ", "#"))
    # print(StringManipulation.format_date("12/31/2019"))
    # print(str_manipulator.index_of_caps("hi"))

    # print(list_manipulator.filter_list())
    # print(list_manipulator.probability(16))
    # print(list_manipulator.chatroom_status())
    # print(list_manipulator.nth_smallest(5))
    # print(list_manipulator.mineral_formation(min_form_list))
    # print(list_manipulator.pops(for_pops_list))
    # print(list_manipulator.count_overlapping(2, for_count_overlapping))
    # print(list_manipulator.tallest_skyscraper(for_skyscraper))
    # print(list_manipulator.sum_primes(for_prime_numbers))
    print(list_manipulator.show_the_love(for_love))
