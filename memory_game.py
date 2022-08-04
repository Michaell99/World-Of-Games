import random
import time
import os


# Setting up these variables as global in order to user the at the global scope


# Making a clear function that would clear the Terminal after the list was shown
def clear():
    os.system("cls")


# Generating a list of numbers that the player would see for 0.7 seconds and guess it also print blank lines in order
# to hide output if clear function can't.
def generate_list(difficulty):
    res = [random.randrange(0, 101, 1) for i in range(difficulty)]
    print(res)
    time.sleep(0.7)
    print('\n' * 100)
    return res


# Letting the player guess the numbers that were shown to him
def get_user_sequence(res):
    user_list = []
    print("Please enter the numbers one by one that were presented to you earlier traveller ")
    while not len(user_list) > len(res) - 1:
        choices = int(input())
        user_list.append(choices)
    else:
        if len(user_list) == len(res):
            return user_list


# Comparing the generated list to the original list of numbers
def list_check(user_list, res):
    if user_list == res:
        return True
    else:
        return False


# Starting the game and also letting the player see the correct list of numbers
def play(difficulty):
    res = generate_list(difficulty)
    clear()
    user_list = get_user_sequence(res)
    if not list_check(user_list, res):
        print('The correct numbers were', '', res)

    else:
        print("Good job traveller you chose the correct numbers")
