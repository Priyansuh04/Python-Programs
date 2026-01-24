# import random

# guess_number = random.randint(1,10)

# while True:
#     user = int(input("enter the number:"))
#     if guess_number == user :
#         print("condition is true")
#         break
#     else:
#         print("condition is not true")


s = {1,2,3,4,5}
lst =list(s)
print(lst)
lst.append(6)
print(lst)
print(s)
new_set = set(lst)
print(new_set)