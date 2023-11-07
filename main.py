import time


# asking the name and adding hour variable
hour = int(time.strftime("%H"))
name = input("Enter your name: ")

# conditions
if 0 <= hour <= 12:
    print(f"Good Morning {name}")

elif 13 <= hour <= 18:
    print("Good afternoon {}".format(name))

else:
    print(f"Good night {name}")
