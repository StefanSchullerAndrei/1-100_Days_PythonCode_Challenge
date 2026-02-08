# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]
# key provided does not exist in the dictionary

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruti = fruit_list[3]
# in this case we have a list, and we try to get a hold of an item from this list with an index that does not exist 

#TypeError
# text = "abc"
# print(text + 5)
# string + integer can't 

# try: Something that might cause an exception
# except: Do this if there wan an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens 

#FileNotFound
# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt", "w"):
#This is a script that works for the pycharm IDE to create the file in the same folder as the script. Running this script in vscode will create the file in the workspace folder, which is not what we want.
    
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "a_file.txt")
try:
    file = open(file_path)
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdsds"]) #this line will give a KeyError.
except FileNotFoundError:
    file = open(file_path, "w")
    file.write("Something")
#This is a script for vscode that will create the file in the same folder as the script.
