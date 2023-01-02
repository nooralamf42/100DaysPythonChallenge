from art import logo, vs, winner
import random
from replit import clear
#print logo
print(logo)

#import list
from game_data import data

score=0
A = "Compare A"
B = "Against B"

#create a dictionary picker
def dictionary_picker():
    random_number = random.randint(0, (len(data) - 1))
    picked_dictionary = data[random_number]
    data.remove(picked_dictionary)
    return picked_dictionary

#info printer
def print_info(info,dic):
  return print(f"\n{info} : {dic['name']}, a {dic['description']}, from {dic['country']}."
    )
  
should_continue = True
b=dictionary_picker()
while should_continue:
  a=b
  b=dictionary_picker()
  a_score = a["follower_count"]
  b_score = b["follower_count"]
  print_info(A,a)
  print (vs)
  print_info(B,b)
   
  user_input = (input("\nWhich do you think have most followers?\nType 'a' for A and 'b' for B : ")).lower()
  clear()
  print(logo)
  if user_input=="a":
    if a_score>b_score:
      score+=1
      if len(data):
        print(f"You guessed right! Current score is {score}.")
    else:
      should_continue = False
      print(f"Ngek wrong guess! Total score is {score}.")
  elif user_input=="b":
    if b_score>a_score:
      score+=1
      if len(data):
        print(f"You guessed right! Current score is {score}.")
    else:
      should_continue = False
      print(f"Ngek wrong guess! Total score is {score}.")
  if not should_continue:
    if(input("Hit enter to restart ...")==""):
      clear()
      print(logo)
      should_continue=True    
  if not len(data):
   print(f"{winner}\nCongratulations! You won this game.")
   should_continue=False
  
  
      
      




















  
