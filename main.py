from art import logo,bust,lose,win,draw
from replit import clear
import random

start_true=True
while start_true:
  start = input("Do you to want to play?\nType 'y for yes or 'n' for no : ")
  if start=="n":
    start_true=False
    clear()
    print("\nHave a good day!")
    
  elif start!="n" and start!="y":
    clear()
    print("\nType corrent input letter!\n")

  else:
    start_true=False
       
def black_jack():
  """to start black jack game"""
  clear()
  print(logo)
  sum_of_computer_cards = 0
  sum_of_user_cards = 0
  computer_cards = []
  user_cards = []
  
  should_continue=2
  while should_continue:
      def card_picker():
        """to pick random cards"""
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        pick=random.randint(0,12)
        card_picked = cards[pick]
        if sum_of_user_cards>21 or sum_of_computer_cards>21 and card_picked==11:
            card_picked=1    
        return (card_picked)
        
      def cards_adder(cards):
        """to add the values of cards"""
        sum_of_cards=0
        for add in cards:
          sum_of_cards+=add
        return sum_of_cards
       
      if should_continue==1:
          give_cards=1
      else:
          give_cards=2
      while give_cards:
        if sum_of_computer_cards<17:
          computer_cards.append(card_picker())
        user_cards.append(card_picker())
        give_cards-=1
      
      sum_of_computer_cards = cards_adder(computer_cards)
      sum_of_user_cards = cards_adder(user_cards)

      if sum_of_user_cards>21:
        should_continue=False
        print(f"{bust}\nYou went over you lose 😥.")
        print(f"\n  Computer cards : {computer_cards}\n    Sum of computer cards is {sum_of_computer_cards}.")
        print(f"  Your cards : {user_cards}\n    Sum of your cards is {sum_of_user_cards}.")
                
        continue_restart=True
        while(continue_restart):
          restart=(input("\nDo you want to play again?\nType 'y' for yes and 'n' for no: "))
          if restart=="y":
            black_jack()
          elif(restart=="n"):
            continue_restart=False
            clear()
            print("\nHave a good day!")
          else:
              print("\nType a valid input letter!")
            
      if(should_continue!=False):
        print(f"\n  Computer's First Card : {computer_cards[0]}")
        print(f"  Your cards : {user_cards}")
        print(f"  Sum of your cards {sum_of_user_cards}\n")

        ask_choice=True
        while ask_choice:
          choice=input("If you want to pick another card type 'p' and to show cards type 's' : ")
          if choice=="p":
            should_continue=1
            ask_choice=False
          elif choice!="s":
            print("\nType a valid input letter!")
          elif choice=="s":
            ask_choice=False
            if sum_of_computer_cards>21:
              print(f"{win}\nComputer went over!!!\nYOU WON 😍.")
              print(f"  Your cards : {user_cards}\n  Sum of your cards is {sum_of_user_cards}.")
              print(f"  Computer cards : {computer_cards}\n  Sum of computer's card is {sum_of_computer_cards}.")
            elif sum_of_computer_cards>sum_of_user_cards:
              print(f"{lose}\nYou have lost the game 😥.")
              print(f"  Your cards : {user_cards}\n  Sum of your cards is {sum_of_user_cards}.")
              print(f"  Computer cards : {computer_cards}\n  Sum of computer's card is {sum_of_computer_cards}.")
            elif sum_of_computer_cards==sum_of_user_cards:
              print(f"{draw}\nThis match is Draw. Nobody wins 😶.")
              print(f"  Your cards : {user_cards}\n  Sum of your cards is {sum_of_user_cards}.")
              print(f"  Computer cards : {computer_cards}\n  Sum of computer's card is {sum_of_computer_cards}.")
            else:             
               print(f"{win}\nYOU WON 😍.")
               print(f"  Your cards : {user_cards}\n  Sum of your cards is {sum_of_user_cards}.")
               print(f"  Computer cards : {computer_cards}\n  Sum of computer's card is {sum_of_computer_cards}.")
              
            continue_restart=True
            while(continue_restart):
              restart=(input("\nDo you want to play again?\nType 'y' for yes and 'n' for no: "))
              clear()
              if restart=="y":
                black_jack()
              elif(restart=="n"):
                continue_restart=False
                should_continue=False
                clear()
                print("\nHave a good day!")                
              else:
                  print("\nType a valid input letter!\n")
black_jack()