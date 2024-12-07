# For loop
import random

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

student_scores = [150, 142, 184, 121, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)

# EXERCISE NO.1
# Using the previous list, print the highest score
max_score = 0   #defining the highest score as 0
for score in student_scores:
    # compare the high score defined against the scores from the list
    if score > max_score:
        #keeping the highest value encountered and saving it in the highscore variable
        max_score = score

print(max_score)

#-----------------------------------------------------

# range will not take the large number entered as a limit
# using "," in the range definition is defining the step ie: range(1 , 12, 3) -> step 3

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)

# EXERCISE NO.2
# FIZZBUZZ
# Your program should print each number from 1 to 100 in turn and include number 100.

# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
    # order matters in if statements so the most complex goes first
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# ------------------------------------------------------------------------------------------------------------
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s","t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S","T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [".", "!", "?", "@", "#", "$", "%", "^", "&", "*", "()", "_", "-", "+", "=", "[]", "{}"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you ike in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy level

# password = ""
#
# for char in range(1,nr_letters + 1):      # or range(0, nr_letters)
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

#----------------------------------------------------------

# Hard level

password_list = []

for char in range(0,nr_letters):      # or range(0, nr_letters)
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")