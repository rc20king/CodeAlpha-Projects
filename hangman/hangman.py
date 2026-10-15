"""
CodeAlpha Internship - Task: Hangman Game
A simple text-based Hangman game.
Concepts used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "internship", "program", "keyboard", "developer"]
MAX_WRONG = 6

STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def display_word(word, guessed):
    """Return the word with unguessed letters hidden as underscores."""
    shown = ""
    for letter in word:
        if letter in guessed:
            shown += letter + " "
        else:
            shown += "_ "
    return shown.strip()


def play():
    word = random.choice(WORDS)
    guessed = []      # all letters guessed so far
    wrong = 0

    print("=" * 30)
    print("      WELCOME TO HANGMAN")
    print("=" * 30)
    print(f"Guess the word, one letter at a time. You can miss {MAX_WRONG} times.")

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print("\nWord:", display_word(word, guessed))
        print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "none")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        guess = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue
        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Win check: every letter of the word has been guessed
        if all(letter in guessed for letter in word):
            print("\nWord:", display_word(word, guessed))
            print(f"\nCongratulations! You won! The word was '{word}'.")
            return

    # Loop ended because wrong == MAX_WRONG
    print(STAGES[MAX_WRONG])
    print(f"\nGame over! You ran out of guesses. The word was '{word}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
