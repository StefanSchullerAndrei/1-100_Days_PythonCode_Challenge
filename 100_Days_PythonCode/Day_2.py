#Data types
# using the [] allows the user to select what character from that string to be printed.
print("Hello"[4]) #will print "O"
print("Hello"[-2]) #will print "l"

# String
print("123" + "345") #Will print 123345 "Concatenation

# Integer = Whole number
print(123 + 345) #Will print the sum

# Large integers
print(123_456_789) #For large numbers, in python it is used _ to allow the user to better visualize the numbers

# Float = Floating Point numbers  (for decimal numbers)
print(3.14159)

# Boolean
print(True)
print(False)

street_name = "Abbey Road"
print(street_name[4] + street_name[7]) #Will print "yo". It takes in counting the spaces as well

len("12345")
print(type("12345")) # will print the type of data
print(type(123))
print(type(12.45))
print(type(True))

print("123" + "345") #Will print the concatination
int("123") #will convert the data from string to integer
print(int("123") + int("345")) #will treat them as integers(numbers) and will print the sum of the two numbers


# print("Number of letters in your name: " + len(input("Enter your name: ")))
name = input("Enter your name: ")
print("Number of letters in your name: " + str(len(name)))

# using the / operator will return a float type result even if the operation is clean
print(6 / 3)

# using the ** raises the power ->2 to the power of 6
print(2 ** 6)

# THE RULE used to do math operations is PEMDAS = ( ) -> ** -> * / -> + -
# PEMDAS = Parentheses -> Exponents -> Multiplication -> Division -> Addition -> Subtraction

print(3 * 3 + 3 / 3 - 3)

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)

round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14

print(round(bmi, 2)) #rounding the result to two decimals

score = 0

#User scores a point

score +=1
print(score)

# f-string
score = 0
height = 1.8
is_winnning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winnning}")

# Day 2 Final Exercise
# We're going to build a tip calculator.
# If the bill was $150.00, split between 5 people, with 12% tip.
# (150.00 / 5) * 1.12 = 33.6
print("Welcome to the tip calculator!")
initial_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = float(initial_bill / people) * (1 + percentage_tip / 100)
final_bill_per_person = round(bill_per_person, 2)

print(f"Each person should pay: ${final_bill_per_person}")
