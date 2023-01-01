#Number Guessing Game
import random
from logo import logo

print(logo)
print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 to 100")
print(
    "NOTE : When you guess a number make sure you input a number not any letter or special character.\nHard difficulty will give you 5 guess chances and easy will give you 10 chance."
)

selected_number = random.randint(1, 100)
# print("psst selected number is",selected_number)


def ask_level():
    level = input(
        "\nChoose a difficulty level.\nType 'easy' for easy and 'hard' for hard : "
    )
    if level == "easy":
        life = 10
    elif level == "hard":
        life = 5
    else:
        print("\nType a valid input!")
        ask_level()

    def check_guess(input_guess):
        if input_guess > selected_number:
            return 1
        elif input_guess == selected_number:
            return 0
        else:
            return -1

    while life:
        guess = int(input("\nType your guess : "))
        checked_guess = check_guess(guess)
        if checked_guess == 1:
            life -= 1
            print(f"  Guessed number is too high.(Remaining guess = {life}).")
        elif checked_guess == 0:
            break
        else:
            life -= 1
            print(f"  Guessed number is too low.(Remaining guess = {life}).")

    if life > 0:
        print(
            f"\nYOU WON !\n  Guessed Number = {guess}\n  Picked Number = {selected_number}"
        )

    elif life == 0:
        print("\nYou LOSE 😥\n  You ran out of life.")
      
    def restart_loop():
      restart_game=input("\nDo you want to play again?\nType 'y' for yes and 'n' for no : ")
      if restart_game=='y':
        clear()
        ask_level()
      elif restart_game=='n':
        print("\nHave a good day!")
      else:
        restart_loop()
    restart_loop()
ask_level()