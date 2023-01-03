# to import data
# import clear
from replit import clear

from data import MENU, resources

# TODO 1: ask for input
def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 1 (a): check the input and choose what to do accordingly

    def check(data_name):
        global data
        data = MENU[data_name]["ingredients"]
        data_water = data["water"]
        data_milk = data["milk"]
        data_coffee = data["coffee"]
        if resources['water'] >= data_water and resources['milk'] >= data_milk and resources['coffee'] >= data_coffee:
            return True
        else:
            return False

    def price(coffee_name):
        data_price = MENU[coffee_name]["cost"]
        return data_price

    if user_input == "off":
        clear()

    elif user_input == "report":
        print(f"\nRemaining Water = {resources['water'] } ml")
        print(f"Remaining Milk = {resources['milk']} ml")
        print(f"Remaining Coffee = {resources['coffee']} gm")
        print(f"Earned Money = {resources['money']}$")
        if input("Press enter to get coffee....\n") == "":
            coffee_machine()

    elif check(user_input):
        print("\nInsert Coins :")
        money = (int(input("Quarter : "))) * 0.25
        money += (int(input("Dimes : "))) * 0.10
        money += (int(input("Nickle : "))) * 0.05
        money += (int(input("Pennie : "))) * 0.01

        coffee_price = price(user_input)
        remaining_money = money - coffee_price

        if money < coffee_price:
            print("you are not getting any coffee")
        else:
            resources["money"] += coffee_price
            resources["water"] -= data["water"]
            resources["milk"] -= data["milk"]
            resources["coffee"] -= data["coffee"]
            print(f"\nHere's your {user_input} ☕")
            if money > coffee_price:
                print(f"    Your {remaining_money}$ change")
            if input("Press enter to get more coffee....") == "":
                coffee_machine()

    elif not check(user_input):
        print("Sorry we don't have enough resources please pick another type of coffee")


coffee_machine()

