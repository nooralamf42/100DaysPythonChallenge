#prime number checker
#Write your code below this line 👇
import math
def prime_checker(number):
        div_number=math.ceil(number/2) 
        while div_number<=number:
          if number%div_number==0 and div_number!=1:
            return f"{number} is not a prime number"
          else:
            return f"{number} is a prime number"
          div_number-=1
          
          
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
print(prime_checker(number=n))