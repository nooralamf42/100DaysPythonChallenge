rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game=[rock,paper,scissors]

user= int(input("Type 1 for rock, 2 for paper and 3 scissor : "))

import random
computer=random.randint(1,3)

if(computer==1 and user==3 or computer==2 and user==1 or computer==3 and user==2 and computer!=user):
  print(f"You choosed : {game[user-1]}")
  print(f"Computer choosed : {game[computer-1]}")
  print("computer wins")
  
if(user==1 and computer==3 or user==2 and computer==1 or user==3 and computer==2 and user!=computer):
  print(f"You choosed : {game[user-1]}")
  print(f"Computer choosed : {game[computer-1]}")
  print("user wins")

if(computer==user):
  print(f"You choosed : {game[user-1]}")
  print(f"Computer choosed : {game[computer-1]}")
  print("Draw")