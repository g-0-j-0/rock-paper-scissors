import random
n=0
lst=["rock","paper","scissors"]
while n!="end":
    n=input()
    x=random.choice(lst)
    print(x)
