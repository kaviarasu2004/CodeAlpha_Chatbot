"""
CodeAlpha - Task 1: Hangman Game
A simple console-based Hangman game.
"""

import random

WORDS = ["python", "hangman", "developer", "internship", "keyboard"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]


def choose_word():
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time. You have", MAX_WRONG_GUESSES, "wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: ", display_progress(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!\n")
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_STAGES[wrong_guesses])
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses += 1
            print(f"Wrong guess. {MAX_WRONG_GUESSES - wrong_guesses} guesses left.\n")

    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
