# higher_lower_game.py

import random
from tollywood_data import data

def get_random_celebrity():
    return random.choice(data)

def format_celebrity(account):
    return f"{account['name']}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def play_game():
    score = 0
    game_should_continue = True

    account_a = get_random_celebrity()
    account_b = get_random_celebrity()

    while game_should_continue:
        while account_a == account_b:
            account_b = get_random_celebrity()

        print(f"\nCompare A: {format_celebrity(account_a)}")
        print("VS")
        print(f"Compare B: {format_celebrity(account_b)}")

        guess = input("Who has more Instagram followers? Type 'A' or 'B': ").lower()

        a_followers = account_a['followers']
        b_followers = account_b['followers']

        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"✅ Correct! Current score: {score}")
            account_a = account_b
            account_b = get_random_celebrity()
        else:
            game_should_continue = False
            print(f"❌ Wrong! Final score: {score}")
            print(f"{account_a['name']}: {a_followers}M | {account_b['name']}: {b_followers}M")

# Start the game
if __name__ == "__main__":
    play_game()
