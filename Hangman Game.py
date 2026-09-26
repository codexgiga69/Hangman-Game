"""
Simple Hangman Game
--------------------
Concepts used: random, while loop, if-else, strings, lists
"""

import random

# Predefined list of words to choose from
WORD_LIST = ["python", "hangman", "computer", "keyboard", "science"]
print("Choose from the words: python, hangman, computer, keyboard, science")


MAX_INCORRECT_GUESSES = 6


def choose_word():
    """Pick a random word from the word list."""
    return random.choice(WORD_LIST)


def display_progress(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []      # letters the player has guessed (correct or not)
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.\n")
    print(f"Guess from the given words: python, hangman, computer, keyboard, science\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(f"Word: {display_progress(word, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check win condition: every letter of the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        # This runs if the while loop exits because incorrect_guesses == MAX_INCORRECT_GUESSES
        print(f"Game over! You've used all {MAX_INCORRECT_GUESSES} incorrect guesses.")
        print(f"The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
