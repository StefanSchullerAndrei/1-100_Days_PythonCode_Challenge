import random
from xml.dom.minidom import ProcessingInstruction

# List comprehension

# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# name = "Andrei"
# letters_list = [letter for letter in name]
#
# range (1, 5)
# range(1, 5)
# range_list = [num * 2 for num in range(1,5)]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]   #Printing the names that have less than 5 characters
# long_names = [name.upper() for name in names if len(name) > 5] #Printing the names that have more than 5 characters


"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

You are going to write a List Comprehension to create a new list called squared_numbers.
This new list should contain every number in the list numbers but each number should be squared. e.g. 4 * 4 = 16 4 squared equals 16.
**DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop.
Target Output [1, 1, 4, 9, 25, 64, 169, 441, 1156, 302"""

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [squared ** 2 for squared in numbers]
# print(squared_numbers)

"""Filtering Even Numbers
In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.

First, use list comprehension to convert the list_of_strings to a list of integers called numbers.

Then use list comprehension again to create a new list called result.

This new list should only contain the even numbers from the list numbers.

Again, try to use Python's List Comprehension instead of a Loop."""

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(numbers) for numbers in list_of_strings]
# result = [even for even in numbers if even % 2 == 0]

"""
Data Overlap

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files."""


# with open('file1.txt') as file1:
#     file1_numbers = file1.readlines()
#
# with open('file2.txt') as file2:
#     file2_numbers = file2.readlines()
#
# numbers1 = [int(num) for num in file1_numbers]
# numbers2 = [int(num) for num in file2_numbers]
#
# result = [num for num in numbers1 if num in numbers2]

# print(result)

"""DICTIONARY COMPREHENSION"""
#new_dict = {new_key:new_value for item in list}
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {students:random.randint(1, 100) for students in names}

"""CONDITIONAL DICTIONARY COMPREHENSION"""
#new_dict = {new_key:new_value for (key, value) in dictionary.items() if test}
passed_students = {students:score for (students, score) in students_scores.items() if score >= 60}

"""You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   

Try Googling to find out how to convert a sentence into a list of words.  *

*Do NOT** Create a dictionary directly.

Try to use Dictionary Comprehension instead of a Loop. 



To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8."""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

