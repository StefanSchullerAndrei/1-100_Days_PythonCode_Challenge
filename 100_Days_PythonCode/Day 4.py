import random
#
# random_integer = random.randint(1, 10)
# print(random_integer)


# random_numer_0_to_1 = random.random() * 10
# print(random_numer_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# EXERCISE NO. 1 - Heads or Tails
# Create a coin flip program. It should randomly print "Heads" or "Tails" everytime it is run.

random_heads_or_tails = random.randint(0, 1)

# assigning Heads and Tails to each outcome.

if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# The items/information stored in a list
states_of_america = ["Delaware" , "Pennsylvania", "New Jersey", "Georgia"]

#print(states_of_america[1]) # The index number counter starts from 0 from left to right. In this case, the item printed from the list will be Pennsylvania

states_of_america[1] = "Pencilvania" # the item with index 1 will be updated with the new value

states_of_america.append("Angelaland") # adding only one new item in the list. the new items will be added at the end of the list

states_of_america.extend(["Angelaland", "Jack Bauer Land"]) # adding more items in the list

print(states_of_america)

# EXERCISE NO. 2 - Who will pay the bill?

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# unlucky_winner = random.choice(friends) # Method number 1 (long run)
# print(unlucky_winner)
print(random.choice(friends)) # Method number 2 (short run)
random_index = random.randint(0, 4)
print(friends[random_index]) # Method number 3

# combining a lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# printing from second list the item with index 1.
print(dirty_dozen[1][1]) # the first index will call the first list and the second index will call the item with the index wanted.

#Exercise NO. 3
# Rock, Paper, Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# METHOD 1

# game_list = [rock, paper, scissors]
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# computer_choice = random.choice(game_list)
# if user_choice == 0:
#     print(game_list[0])
#     print(f"Computer chose:")
#     print(computer_choice)
#     if computer_choice == game_list[0]:
#         print("It's a draw!")
#     elif computer_choice == game_list[1]:
#         print("You lose!")
#     elif computer_choice == game_list[2]:
#         print("You win!")
# elif user_choice == 1:
#     print(game_list[1])
#     print(f"Computer chose:")
#     print(computer_choice)
#     if computer_choice == game_list[0]:
#         print("You win!")
#     elif computer_choice == game_list[1]:
#         print("It's a draw!")
#     elif computer_choice == game_list[2]:
#         print("You lose!")
# elif user_choice == 2:
#     print(game_list[2])
#     print(f"Computer chose:")
#     print(computer_choice)
#     if computer_choice == game_list[0]:
#         print("You lose!")
#     elif computer_choice == game_list[1]:
#         print("You win!")
#     elif computer_choice == game_list[2]:
#         print("It's a draw")
#
# -----------------------------------------------------------------------------------------------------------------
#
#METHOD 2

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0  and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
