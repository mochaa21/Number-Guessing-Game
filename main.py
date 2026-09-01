import random
import time

angka_rand = random.randint(1, 100)
chance = 0
attempts = 0

print(f"\n\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
print("\n-----==========-----")

x = int(input(f"Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\nEnter your choice -> "))

if x == 1:
    chance = 10
    print(f'Great! You have selected the Easy difficulty level. Your chance is {chance}')
elif x == 2:
    chance = 5
    print(f'Great! You have selected the Medium difficulty level. Your chance is {chance}')
elif x == 3:
    chance = 3
    print(f'Great! You have selected the Hard difficulty level. Your chance is {chance}')
else:
    print("Your input is invalid")
print('\n-----==========-----')

while chance > 0:
    try:
        print('Selecting a number to guess...')
        time.sleep(2.5)
        user_inp = int(input('The numbers have been selected! Enter your guess -> '))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    attempts += 1
    if user_inp == angka_rand:
        print('process..')
        time.sleep(2.5)
        print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
        break
    elif user_inp > angka_rand:
        chance -= 1
        print('process..')
        time.sleep(2.5)
        print('too small..')

if chance == 0:
    print(f'Game over! the correct number is {angka_rand}')