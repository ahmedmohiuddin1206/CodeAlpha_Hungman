import random

words = ["python", "computer", "program", "coding", "developer"]

word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

while incorrect_guesses < max_incorrect_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "\n")

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        print("The word was:", word)
        break

if incorrect_guesses == max_incorrect_guesses:
    print("Game Over!")
    print("The word was:", word)