import random

print("Welcome to the Number Guessing Game!")
difficulty = input("What difficulty do you want? 'easy', 'medium', or 'hard' ")
game_on = True
already_guessed = []

if difficulty == "hard":
    guesses_left = 20
    number = random.randint(1, 1000)
elif difficulty == "medium":
    guesses_left = 15
    number = random.randint(1, 500)
else:
    guesses_left = 10
    number = random.randint(1, 100)

while game_on:
    guess = int(input("What number do you guess? "))
    if guess in already_guessed:
        print(f"You already guessed {guess}.")
        continue
    elif guess == number:
        print("Correct!")
        print("You win!")
        quit()
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")

    already_guessed.append(guess)
    guesses_left -= 1
    print(f"You only have {guesses_left} guesses left.")
    if guesses_left == 0:
        print(f"You lose. The number was {number}.")
        quit()
