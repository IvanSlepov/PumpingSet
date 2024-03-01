# Task 7. Chat Room Status
# Write a function chatroom_status() that returns the number of users in a chatroom based on the following rules:
#
# If there is no one, return “no one online”.
# If there is 1 person, return “user1 online”.
# If there are 2 people, return user1 and user2 online”.
# If there are n>2 people, return the first two names and add “and n-2 more online”.
# For example, if there are 5 users, return:
#
# "user1, user2 and 3 more online"
# Examples
#
# chatroom_status([]) ➞ "no one online"
# chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"
# chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"
# chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]) ➞ "pap_ier44, townieBOY and 4 more online"

def chatroom_status(users_online_list):
    number_of_users_in_the_list = len(users_online_list)

    if number_of_users_in_the_list == 0:
        print("no one online")
    if number_of_users_in_the_list == 1:
        print(f"{users_online_list[0]} online")
    if number_of_users_in_the_list == 2:
        print(f"{users_online_list[0]} and {users_online_list[1]} online")
    if number_of_users_in_the_list > 2:
        print(f"{users_online_list[0]}, {users_online_list[1]} and {len(users_online_list) - 2} more online")
