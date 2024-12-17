def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))
# print(formated_string)
#
# def function_1(text):
#     return text + text
#
# def function_2(text):
#     return text.title()
#
# output = function_2(function_1("Hello"))
# print(output)


"""
Write a program that returns True or False whether if a given year is a leap year.

This is how you work out whether if a particular year is a leap year. 

- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder """


def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False


is_leap_year(2024)

# ----------------------------------------------------
# DOCSTRINGS

def format_name(f_name, l_name):
    """Take a first and last name and format
    it to return the title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name()

length = len(formatted_name)