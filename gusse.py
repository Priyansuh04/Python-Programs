import random

guess_number = random.randint(1,10)

while True:
    user = int(input("enter the number:"))
    if guess_number == user :
        print("condition is true")
        break
    else:
        print("condition is not true")