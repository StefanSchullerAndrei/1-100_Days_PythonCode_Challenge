def greet():
    print("Hello")
    print("Welcome to Day 8 of coding!")
    print("Enjoy!")

greet()

# Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Welcome to Day 8 of coding {name}!")

greet_with_name("Andrei")

# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x weeks left.
#
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

def life_in_weeks(age):
    total_years = 90
    years_left = total_years - age
    X = years_left * 52

    print(f"You have {X} weeks left.")


life_in_weeks(12)

#You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.

# 2. Then check for the number of times the letters in the word LOVE occurs.
 
# 3. Then combine these numbers to make a 2 digit number and print it out.

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2)
    lower_names = combined_names.lower()
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    first_digit = t + r + u + e

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    second_digit = l + o + v + e

    love_score = str(first_digit) + str(second_digit)
    print(love_score)


calculate_love_score("Mihaela", "Teodor")

# ----------------------------------------------------------------------

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s","t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S","T", "U", "V", "W", "X", "Y", "Z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Tyoe your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# TODO-1: Create a function called 'encrypt() that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2; Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet by the shift amount and print the encrypted text.

def encrypt(original_text, shift_amount):
    cipher_text = ""

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount  # 7 -> 9

        shifted_position %= len(alphabet)  # 0-25
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")



# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message
# encrypt(original_text=text, shift_amount=shift)

# -------------------------------------------------------------------
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# encrypt(original_text=text, shift_amount=shift)
# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# def decrypt(original_text, shift_amount):
#     output_text = ""
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#
#     print(f"Here is your decoded result: {output_text}")
# decrypt(original_text=text, shift_amount=shift)

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1

#         shifted_position = alphabet.index(letter) + shift_amount

#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")


# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# --------------------------------------------------------------------------------------------------
#  ------------------------------FINAL VERSION CAESAR CIPHER VERSION -------------------------------
# TODO-1: Import and print the logo from art.py when the program starts.

# from art import logo
# print(logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # TODO-2: What happens if the user enters a number/symbol/space?


# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     if encode_or_decode == "decode":
#         shift_amount *= -1
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text  += letter
#         else:


#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")


# # TODO-3: Can you figure out a way to restart the cipher program?
# should_continue = True

# while should_continue:

#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye!")
