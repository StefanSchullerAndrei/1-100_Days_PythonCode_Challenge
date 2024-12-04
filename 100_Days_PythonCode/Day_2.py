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

print(round(bmi))
