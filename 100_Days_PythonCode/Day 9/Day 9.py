programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Dictionaries have elements that are identified by their key
print(programming_dictionary["Function"])

# Adding data in the dictionaries

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# empty_dictionary = {}  # Creating a new and empty dictionary
# empty_dictionary = []  # Adding data in dictionaries

# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# ----------------------------------------------------------
# Grading Program
# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.
#
# Write a program that converts their scores to grades.

# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# ------------------------------------------------------------