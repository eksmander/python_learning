import random

num = random.randint(1, 100)

def one_guess():
    ans = input("pick a number: ")
    ans = int(ans)
    if num > ans:
        print ("to low")
    elif num < ans:
        print ("to high")
    else:
        print ("yes")
    return ans == num

while True:
    found = one_guess()
    if found:
         break