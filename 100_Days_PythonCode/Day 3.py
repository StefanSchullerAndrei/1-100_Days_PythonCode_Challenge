print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")

# find out if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))
# the modulo is written as a percentage sign in Python. It gives you the remainder after a division.

result = number % 2
print(result)
if result == 0:
    print("The number given is an even number.")
else:
    print("The number given is an odd number.")


# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
#
# If the bmi is under 18.5 (not including), print out "underweight"
#
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
#
# If the bmi is 25 (including) or over, print out "overweight"

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")

# MULTIPLE IF (if all conditions are true - you get all executions)
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M OR L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
# todo: work out how much they need to pay based on their size choice.
size = input("What size pizza do you want? S, M OR L: ")
if size == "S":
    bill = 15
    print("That would be $15")
elif size == "M":
    bill = 20
    print("That would be $20")
elif size == "L":
    bill = 25
    print("That would be $25")
else:
    print("You typed the wrong inputs.")

# todo: work out how much to add to their bill based on their pepperoni choice.
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 3
        print("That would be an extra of $3.")
    if size == "M":
        bill += 4
        print("That would be an extra of $4.")
    if size == "L":
        bill += 5
        print("That would be an extra of $5.")
# todo: work out their final amount based on whether if they want extra cheese.
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    if size == "S":
        bill += 2
        print("That would be an extra of $2.")
    if size == "M":
        bill += 3
        print("That would be an extra of $3.")
    if size == "L":
        bill += 4
        print("That would be an extra of $4.")

print(f"The total amount for the pizza is ${bill}")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
print("Every choice you make will decide your fate!")
first_choice = input("You're at a cross road. Where do you want to go? \n Left or Right?\n").lower()
if first_choice == "left":
    # Continue the game
    second_choice = input("You've come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_choice == "wait":
        # game will continue
        third_choice = input("You arrive at the island unharmed. "
                             "There is a house with 3 doors. One red, "
                             "one yellow and one blue. "
                             "Which colour do you choose?\n").lower()
        if third_choice == "red":
            print("It's a room full of fire. Game over")
        elif third_choice == "yellow":
            print("You found the treasure. You win!")
        elif third_choice == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn;t exist. Game Over.")

    else:
        print("You got attacked by an angry trout. Game Over!")

else:
    print("You fell into a hole. Game Over!")
