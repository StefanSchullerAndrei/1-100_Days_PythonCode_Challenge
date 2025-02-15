with open("my_file.txt") as file:       #OPENING THE CONTAINS OF A FILE TEXT
    contents = file.read()
    print(contents)

# with open("my_file.txt", mode="a") as file:   #Adding new text/contains to a file
#     file.write("\nNew text.")
#
# with open("new_file.txt", mode="w") as file:      #Creating a new .txt file with text in it
#     file.write("New text")


# with open(r"C:/Users/andre/OneDrive/Desktop/new_file.txt") as file:  #Opening a file from a different location
#     contents = file.read()
#     print(contents)

