import random
from art import logo, vs
from game_data import data


def get_random_data():
    """Get random data and return the values"""
    return random.choice(data)


def format_data(account):
    """Takes the account data and returns it in printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_place = account["country"]
    return f"{account_name}, a {account_description}, from {account_place}."


def check_answer(guess, a_follower, b_follower):
    """Takes the guess and follower counts and checks if the answer is correct or not."""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = get_random_data()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers?Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right!! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. The final score is {score}.")
            game_should_continue = False


game()
