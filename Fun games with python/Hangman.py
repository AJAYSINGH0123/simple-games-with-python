import random

def hangman():
    words = ["python", "java", "kotlin", "javascript"]
    word_to_guess = random.choice(words)
    guessed_letters = set()
    attempts = 6
    guessed_word = ["_" for _ in word_to_guess]

    while attempts > 0 and "_" in guessed_word:
        print(" ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("You lost! The word was:", word_to_guess)

hangman()
