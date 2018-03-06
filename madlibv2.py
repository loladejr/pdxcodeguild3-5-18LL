import random
Name=input("What is nickname" ":").split(",")
location=input("enter your favorite place"":").split(",")
country=input("enter a country"":").split(",")
car=input("enter a car model"":").split(",")
reason=input("enter what you like in a car"":").split(",")
color=input("enter a color"":").split(",")


print (" My name is " + random.choice(Name) + "I live in" + random.choice(country) + "My favorite place is" + random.choice(location) + "I like"+ random.choice(car) + "because they drive" + random.choice(reason) + "my favorite car Color is" + random.choice(color))

while True:
    decision=input("do you want to play again")
    if decision != "yes":break
    print (" My name is " + random.choice(Name) + "I live in" + random.choice(country) + "My favorite place is" + random.choice(location) + "I like"+ random.choice(car) + "because they drive" + random.choice(reason) + "my favorite car Color is" + random.choice(color))
