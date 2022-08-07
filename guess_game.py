import random


# generating random number that will be the secret number
def generate_random(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


# Getting the users input
def get_guess(difficulty):
    print(f"please choose a number between 1 and {difficulty}")
    player_guess = input()
    while not player_guess.isnumeric():
        print(f"please choose a number between 1 and {difficulty}")
        player_guess = input()
    return player_guess


# comparing results and letting the player know if he chose right
def compare_results(player_guess, secret_number):
    if int(player_guess) == int(secret_number):
        return True
    else:
        return False


# play function that will start all the game and also let the player choose if he want to play again
def play(difficulty):
    secret_number = generate_random(difficulty)
    player_guess = get_guess(difficulty)
    if not compare_results(player_guess, secret_number):
        print(f"You chose wrong traveler The secret number was", "", secret_number)
    else:
        print("You chose correctly congratulations! ")
    return compare_results(player_guess, secret_number)
