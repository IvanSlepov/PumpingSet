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
from OOP_approach_tasks import task_1_2_5_9_string_and_date_manipulations


print("hello, main.py")

str_manipulator = task_1_2_5_9_string_and_date_manipulations.StringManipulation("gee")

if __name__ == '__main__':
    print(str_manipulator.stutter())
    print(str_manipulator.is_plural("horses"))
    print(str_manipulator.alphabet_soup("damn it"))
    print(task_1_2_5_9_string_and_date_manipulations.StringManipulation.remove_char_from_str
          ("Nice shorts babe.", " ", "#"))
    print(task_1_2_5_9_string_and_date_manipulations.StringManipulation.format_date("12/31/2019"))
