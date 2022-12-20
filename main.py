#FizzBuzz program

x=0;
for no in range(1,101):
  x=int(no)
  if(no%3==0 and no%5!=0):
    print("fizz")
  if(no%5==0 and no%3!=0):
    print("buzz")
  if(no%3==0 and no%5==0):
    print("fizzbuzz")
  if(no%3!=0 and no%5!=0):
    print(x)

