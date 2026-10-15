# Hangman Game - CodeAlpha Internship Task

A simple text-based Hangman game built for the **CodeAlpha** internship. The player guesses a hidden word one letter at a time, with a limited number of wrong guesses.

## Features
- Random word chosen from a list of 5 predefined words
- Maximum of 6 incorrect guesses
- ASCII hangman drawing that updates after each wrong guess (Python version)
- Input validation (single letters only, no repeated guesses)
- Play-again option after each game
- Console input/output only - no graphics or audio

## Concepts Used
`random` | `while` loop | `if-else` | strings | lists

## Project Structure
```
CodeAlpha_HangmanGame/
|-- hangman.py      # Python version
|-- Hangman.java    # Java version
|-- README.md
`-- .gitignore
```

## How to Run

**Python** (3.6+)
```bash
python hangman.py
```

**Java** (JDK 8+)
```bash
javac Hangman.java
java Hangman
```

## How to Play
1. The game picks a random word and shows it as underscores, e.g. `_ _ _ _ _ _`.
2. Enter one letter at a time.
3. Correct letters are revealed in the word; wrong letters cost you one of your 6 lives.
4. Guess the whole word before you run out of lives to win.

## Sample Output
```
Word: p _ t _ o _
Guessed letters: o p t
Wrong guesses left: 5

Enter a letter: y
Good guess! 'y' is in the word.
```

## Author
**Anirudh** - CodeAlpha Intern
