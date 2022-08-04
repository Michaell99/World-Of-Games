from currency_converter import CurrencyConverter
import random


def get_money_interval(difficulty):
    num = random.randint(0, 100)
    print(f'The selected number is {num}$')
    c = CurrencyConverter()
    converted_num = c.convert(num, 'USD', 'ILS')
    min_range = converted_num - (5 - difficulty)
    max_range = converted_num + (5 - difficulty)
    return max_range, min_range, converted_num, num


def user_guess():
    guess_user = float(input("Please enter your guess Traveler \n"))
    return guess_user


def check_user_guess(max_range, min_range, guess_user):
    if max_range >= guess_user >= min_range:
        return True
    else:
        return False


def play(difficulty):
    min_range, max_range, converted_num, num = get_money_interval(difficulty)
    guess_user = user_guess()
    if not check_user_guess(max_range, min_range, guess_user):
        print(f"The correct Rate for that amount of USD is", converted_num, "ILS")
    else:
        print("Good job traveler you chose right")
