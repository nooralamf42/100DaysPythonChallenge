#learning output functions

# def name_format(first_name,last_name):
#   n=0
#   new_f=""
#   for n in range(0,len(first_name)):
#     if n==0:
#       new_f+=first_name[n].upper()
#     else:
#       new_f+=first_name[n].lower()
#   new_l=""
#   for n in range(0,len(last_name)):
#     if n==0:
#       new_l+=last_name[n].upper()
#     else:
#       new_l+=last_name[n].lower()
  
#   return (f"Welcome {new_f} {new_l}.")

f_name = input("Enter your first name : ")
l_name = input("Enter your last name : ")
from replit import clear
clear()

def name_format(first_name,last_name):
  return(f"Welcome {first_name.title()} {last_name.title()}.")
z=(name_format(first_name=f_name,last_name=l_name))
print(z)


#second method

