#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

random.seed = input("Enter random numbers : ")

random_number = random.randint(1, 2)
if (random_number == 1):
    print("Heads")
else:
    print("Tails")
