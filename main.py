import random
import time

angka_rand = random.randint(1, 100)
chance = 0
attempts = 0

print(f"\n\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
print("\n-----==========-----")


while True:
    try:
        x = int(input(f"Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\nEnter your choice -> "))
        if x == 1:
            chance = 10
            print(f'\nGreat! You have selected the Easy difficulty level. Your chance is {chance}')
            break
        elif x == 2:
            chance = 5
            print(f'\nGreat! You have selected the Medium difficulty level. Your chance is {chance}')
            break
        elif x == 3:
            chance = 3
            print(f'\nGreat! You have selected the Hard difficulty level. Your chance is {chance}')
            break
        else:
            print("\n-----=== Your input is invalid! ===-----\n")
            continue
    except ValueError:
        print(f'\n-----=== Error! Input a number (1, 2, 3) ===-----')
        continue

print('\n-----==========-----')

while chance > 0:
    try:
        print('retrieving data..')
        time.sleep(2.5)
        user_inp = int(input('Enter your guess (1, 100) -> '))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if user_inp < 1 or user_inp > 100:
        print("Out of range! Please guess a number between 1 and 100.")
        continue
    
    attempts += 1
    print('processing..')
    if user_inp == angka_rand:
        time.sleep(2.5)
        print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
        break
    elif user_inp < angka_rand:
        chance -= 1
        time.sleep(2.5)
        print(f'Too small! Try a bigger number. (Chances left: {chance})')
    elif user_inp > angka_rand:
        chance -= 1
        time.sleep(2.5)
        print(f'Too big! Try a smaller number. (Chances left: {chance})')

if chance == 0:
    print(f'Game over! the correct number is {angka_rand}')