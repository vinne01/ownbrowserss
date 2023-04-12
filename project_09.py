import random
cnumber=random.randrange(1,101)
userinput=int(input("enter your numbers"))

if userinput > cnumber :
    print("computer number",cnumber)
    print("your guess is high")
elif userinput < cnumber :
    print("computer number",cnumber)
    print("your guess is low")
else:
    print("computer number",cnumber)
    print("your guess number is equal")
