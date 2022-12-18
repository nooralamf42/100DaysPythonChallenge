# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nameA = name1.lower()
nameB = name2.lower()

nameAB=nameA+nameB

nameAB1 = nameAB.count("t")
nameAB1 += nameAB.count("r")
nameAB1 += nameAB.count("u")
nameAB1 += nameAB.count("e")

nameAB2 = nameAB.count("l")
nameAB2 += nameAB.count("o")
nameAB2 += nameAB.count("v")
nameAB2 += nameAB.count("e")

loveScore = nameAB1 * 10 + nameAB2

if (loveScore < 10 or loveScore > 90):
    print(
        f"Your love score is {loveScore}, you go together like coke and mentos."
    )
elif (loveScore >= 40 and loveScore <= 50):
    print(f"Your love score is {loveScore}, you are alright together.")
else:
    print(f"Your loveScore is {loveScore}")
