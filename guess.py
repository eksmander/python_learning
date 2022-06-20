import random

num = random.randint(1, 100)

def one_guess():
    ans = input("pike a numbre: ")
    ans = int(ans)
    if num > ans:
        print ("to low")
    elif num < ans:
        print ("to hiey")
    else:
        print ("yes")
    return ans == num

while True:
    found = one_guess()
    if found:
         break