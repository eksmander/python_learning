val = input("Enter your value: ")

if val == "magic":
    print("Abracadabra")
elif val == "tech":
    print("Woah!")
elif val.startswith("food"):
    print("My favorite food is " + val.replace("food", ""))
else:
    print("What is going on here!?!?!")