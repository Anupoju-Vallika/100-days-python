import random

def number_guessing_game():
    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input(f"\nYou have {attempts} attempts remaining. Make a guess: "))

        if guess == number_to_guess:
            print(f"🎉 Correct! You guessed the number {number_to_guess}!")
            return
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")

        attempts -= 1

    print(f"\n😢 You've run out of guesses. The number was {number_to_guess}.")

# Start the game
number_guessing_game()
