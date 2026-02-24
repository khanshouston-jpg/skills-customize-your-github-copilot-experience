
# 🎮 Assignment: Games in Python — Hangman

## 🎯 Objective

Students will implement a playable Hangman game in Python to practice control flow, string handling, and simple game logic.

## ⚙️ Prerequisites

- Basic Python (variables, loops, conditionals, functions)
- Familiarity with reading/writing files is helpful but optional

## 📦 Files Provided

- `starter-code.py` — minimal scaffold to load a word list and run the game loop
- `README.md` — (this file) assignment instructions

## ⏱️ Estimated Time

45–75 minutes

## 🧭 Difficulty

Beginner → Intermediate

## 📝 Tasks

### 🛠️ Task 1 — Build the Game Core

#### Description
Implement the core Hangman gameplay: word selection, input handling, progress display, and win/lose conditions.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list or `words.txt`
- Accept single-letter guesses and update the displayed progress (e.g., `_ a _ _`)
- Track and display remaining attempts and letters already guessed
- End the game when the word is fully guessed or attempts run out
- Print a clear win or lose message

Deliverable: a script (`hangman.py` or updated `starter-code.py`) that runs from the command line.

### 🛠️ Task 2 — Add Features & Robustness

#### Description
Improve usability and robustness by handling edge cases and adding at least one extra feature.

#### Requirements

- Handle invalid input (non-letters, repeated guesses) gracefully
- Support case-insensitive guesses
- Add at least one enhancement (choose one):
	- Hint system (reveal a letter)
	- Difficulty levels (adjust attempt counts)
	- Persist high scores or attempt history to a file

Deliverable: updated script demonstrating the enhancement and a short note describing your choice.

### 🛠️ Task 3 — Tests & Documentation

#### Description
Provide basic tests and usage instructions so others can run and understand your game.

#### Requirements

- Include a short `README` usage snippet or a `--help` flag
- Add at least one simple unit test or a test script demonstrating game functions (e.g., word selection, guess validation)

Deliverable: usage example in `exploration.txt` or `README.md` and a `tests/` folder or `test_hangman.py`.

## 💡 Hints

- Use `random.choice()` to pick a word from a list
- Represent the current progress as a list of characters for easy updates
- Keep user prompts clear; validate input before processing

## ✅ Submission

1. Add or update `starter-code.py` (or `hangman.py`) with your implementation
2. Include any saved files (`words.txt`, `exploration.txt`, plot images not applicable`) in the assignment folder
3. Add tests or a short `usage` section demonstrating how to run the game

## 🎓 Learning Outcomes

- Build an interactive command-line game using Python
- Apply control flow and string manipulation to a real problem
- Implement input validation and basic testing
