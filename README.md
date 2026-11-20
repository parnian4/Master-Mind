# Master-Mind
mini project for advanced programming
Guess the Password 🎮

About the Project

This is a simple Python number guessing game. The program creates a random 4-digit password using numbers from 1 to 6, without repeating any digits. The player has 10 chances to guess the password.

How the Game Works

- The program generates a random 4-digit password.
- The password contains digits from 1 to 6.
- Repeated digits are not allowed.
- The player has 10 attempts to guess the password.
- After each valid guess, the program shows:
  - Right digits with wrong positions
  - Right digits with right positions
- Invalid guesses do not count as an attempt.
- If the player guesses the password correctly, they win.
- If the player cannot guess the password within 10 attempts, they lose and the correct password is shown.

Technologies Used

- Python
- Random module

How to Run

1. Download or clone the project.
2. Run the Python file.
3. Enter a 4-digit guess using numbers from 1 to 6, without repeating digits.
4. Try to guess the password in 10 attempts.

Example

Enter your guess: 1234

right digits with wrong positions: ['1', '3']
right digits with right positions: ['2']

Enter your guess: ...

Author

A Python beginner project developed for practice.
