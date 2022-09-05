''' By @CoderX on Telegram'''

from time import sleep as _
import time
from os import system as ss
from sys import exit as l
print('''"+" for Addition (Default)
"-" for  substraction
"*" for multiplication
"/" for  division
''')

x = eval(input("Enter first value: "))
y = eval(input("Enter second value: "))
z = input("What operation do you want to perform?: ")
ss('clear')
cz=input('Are you in hurry? \n[Yes/No] enter = yes: ').lower()
ss('clear')
t=4
if cz !='yes' and cz !='no' and "":
  print('Wrong input "{}"\ntry again'.format(cz))
  l()

if cz == 'no':
    print('Calculating...\n')
    while t>=0: 
       mins, secs = divmod(t, 60) 
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print('estimated time:', timer, end="\r") 
       time.sleep(1) 
       t -= 1
else:
    pass

ss('clear')
if z == "-":
    print(f"Answer: {x-y}")
elif z == "":
    print(f"using default operation as you didn't specify any \nAnswer: {x+y}")
elif z == "+":
    print(f"Answer: {x+y}")
elif z == "*":
    print(f"Answer: {x*y}")
elif z == "/":
    print(f"Answer: {x/y}")
elif z == "//":
    print(f"Answer: {x//y}")
elif z == "%":
    print(f"Answer: {x%y}")
else:
    try:
        print("\n\nOperation not supported please check supported operations above")
        print("\n\nStill last try")
        h = eval(input("Enter everything together: "))
        print(f"Answer: {h}")
    except:
        print("\nI'm really sorry either such operation doesn't exists or I can't perform that")
