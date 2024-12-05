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
size = input("What size pizza do you want? S, M OR L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

# todo: work out how much to add to their bill based on their pepperoni choice.

# todo: work out their final amount based on whether if they want extra cheese.