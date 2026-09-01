import random

print(f"\n\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
print("\n-----==========-----")
angka_rand = random.randint(1, 100)

x = int(input(f"Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\nYour choose -> "))

chance = 0
if x == 1:
    chance = 10
elif x == 2:
    chance = 5
elif x == 3:
    chance = 3
else:
    print("Your input is invalid")

print(f"Result submit is {chance} chance")
