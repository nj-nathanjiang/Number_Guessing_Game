import random

print("Welcome to the Number Guessing Game!")
difficulty = input("What difficulty do you want? 'easy', 'medium', or 'hard' ")
game_on = True
already_guessed = []
the_range = []

if difficulty == "hard":
    print("The range will be from 1 to 1000.")
    guesses_left = 20
    number = random.randint(1, 1000)
    for i in range(1, 1001):
        the_range.append(i)
elif difficulty == "medium":
    print("The range will be from 1 to 500.")
    guesses_left = 15
    number = random.randint(1, 500)
    for i in range(1, 501):
        the_range.append(i)
else:
    print("The range will be from 1 to 100.")
    guesses_left = 10
    number = random.randint(1, 100)
    for i in range(1, 101):
        the_range.append(i)

while game_on:
    try:
        guess = int(input("What number do you guess? "))
    except ValueError:
        print("That is not a number!")
        continue
    if guess in already_guessed:
        print(f"You already guessed {guess}.")
        continue
    elif guess not in the_range:
        print("That number is not in the range!")
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
