from replit import clear
from art import logo,winner

print(logo+"Blind Charity helps you to find who is willing to give highest money for charity without showing others name\n")

people_dic={}
should_continue=False

while not should_continue:
  name = input("Type your name : ")
  money = int(input("Enter amount of money that you willing to give : $"))
  decide= input("\nIs there anyone else? Type 'yes' or 'no' : ")

  people_dic[name]=money
  if decide=="yes":
    clear()
    print(logo)
  elif decide=="no":
    clear()
    should_continue=True

charity=0

for person in people_dic:
  if people_dic[person]>charity:
    charity=people_dic[person]
    person_name=person

print(f"{winner}{person_name} is winner!\nGiving ${charity} as charity.")
