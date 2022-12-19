# Bill splitting using split string method
import random

ram = random.seed(input("Type a random number : "))
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

randomname = random.randint(0, len(names))
print(f"{names[randomname]} is gonna pay.")
