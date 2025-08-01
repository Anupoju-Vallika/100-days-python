import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
guessed_letters = []

# Display blanks
display = ['_' for _ in chosen_word]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    # Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good guess! ✅")
    else:
        lives -= 1
        print(f"Wrong! '{guess}' is not in the word. You lose a life. ❌")
        print(stages[6 - lives])
        if lives == 0:
            end_of_game = True
            print("You lost! Game Over. 😢")
            print(f"The word was: {chosen_word}")

    print("Current word: " + " ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You win! 🎉")


