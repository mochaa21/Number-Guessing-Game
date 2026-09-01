import random
import time

print(f"\n\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
print("\n-----==========-----")
angka_rand = random.randint(1, 100)

x = int(input(f"Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\nEnter your choice -> "))

chance = 0
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
    print('Sedang memilih angka untuk ditebak...')
    time.sleep(2.5)
    user_inp = int(input('Angka sudah dipilih! silahkan tebak angka yang aku pilih!\n'))