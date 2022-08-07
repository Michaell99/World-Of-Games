import ast
import time
import guess_game
import memory_game
import Currency_game
import score


def welcome_wog():
    player_name = input("What is your name traveler? ")
    print(f"Hello {player_name} and welcome to the world of games (Wog) here you can find many cool games to play! \n")


def load_game():
    time.sleep(1)
    print("Which game would you like to play? \n"
          "We the following games to play:\n"
          "1.Memory game \n"
          "2.Guess Game \n"
          "3.Currency roulette \n")

    # choosing a game to play
    chosen_game = input()
    while not chosen_game.isnumeric():
        print("Please enter a valid numerical value.")
        chosen_game = input()
    while int(chosen_game) < 1 or int(chosen_game) > 3 and chosen_game.isnumeric():
        print("Please enter a number between 1 to 3.")
        chosen_game = input()

    # Choosing difficulty.
    print("Please choose game difficulty from 1 to 5: ")
    difficulty = input()
    while not difficulty.isnumeric():
        print("Please enter a valid numerical value.")
        difficulty = input()
    while int(difficulty) < 1 or int(difficulty) > 5 and difficulty.isnumeric():
        print("Please enter a number between 1 to 5.")
        difficulty = input()

    # Opening json file With instructions for each game
    my_file = open("instructions.json")
    info = dict(ast.literal_eval(my_file.read()))

    # turning the inputs above to int
    chosen_game = int(chosen_game)
    difficulty = int(difficulty)

    # Letting the player choose if he wants instructions
    help_game = input("Great would you like to get instructions for this game? y/n ""\n").lower()
    if chosen_game == 1 and help_game == "y":
        print(info["memory"])
    elif chosen_game == 2 and help_game == "y":
        print(info["guessing"])
    elif chosen_game == 3 and help_game == "y":
        print(info["currency"])

    # Closing the instructions file
    my_file.close()

    # This part takes the user input for both game and difficulty and runs the game he chose with the difficulty he
    # chose.
    if chosen_game == 1:
        memory_game.play(difficulty)
        if bool(memory_game) is True:
            score.add_score(difficulty)

    elif chosen_game == 2:
        guess_game.play(difficulty)
        if bool(guess_game) is True:
            score.add_score(difficulty)
    else:
        Currency_game.play(difficulty)
        if bool(Currency_game) is True:
            score.add_score(difficulty)
