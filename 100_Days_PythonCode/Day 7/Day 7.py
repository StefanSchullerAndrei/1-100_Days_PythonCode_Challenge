# STEP 1

# import random
#
word_list = ["aardvark", "baboon", "camel"]
#
# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# chosen_word = random.choice(word_list)
# print(chosen_word)
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#
# guess = input("Guess a letter: ").lower()
# print(guess)
#
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
# #  is, "Wrong" if it's not.
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
#
#
# import random
# word_list = ["aardvark", "baboon", "camel"]
#
# chosen_word = random.choice(word_list)
#
# print(chosen_word)
#
# # STEP 2
#
# # TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
# placeholder = ""
# guess = input("Guess a letter: ").lower()
# world_length = len(chosen_word)
# for fine in range(world_length):
#     placeholder += "_"
# print(placeholder)
#
# # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
#
# display = ""
#
# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"
#
# print(display)
#
#
# # STEP 3
#
# # TODO-1: - Use a while loop to let the user guess again
#
# game_over = False
# correct_letters = []
# while not game_over:
#     guess = input("Guess a letter again: ").lower()
#
#     display = ""
#
#
#     # TODO-2: Change the for loop so that you keep the previous correct letters in display
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(letter)  # adding the letter guessed to the list and saving it
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#
#     print(display)
#
#     if "_" not in display:
#         game_over = True
#         print("You win!")


# STEP 4

# # TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #   Set 'lives' to equal 6
# import random
# from hangman_art import stages
#
# lives = 6
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# placeholder = ""
# world_length = len(chosen_word)
# for position in range(world_length):
#     placeholder += "_"
# print(placeholder)
#
#
#
# game_over = False
# correct_letters = []
# while not game_over:
#     guess = input("Guess a letter again: ").lower()
#
#     display = ""
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(letter)  # adding the letter guessed to the list and saving it
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#
#     print(display)
#
#
# # TODO-2: - If guess is not a letter in the 'chosen_word', then reduce 'lives' by '1'
# #         - If 'lives' goes down to '0' then the game should end, and it should print 'You lose'
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("You lose!")
#
#     if "_" not in display:
#         game_over = True
#         print("You win!")
#
# # TODO-3: - print the ASCII art from the list 'stages' that corresponds to the current number of 'lives' the user has remaining
#
#
#     print(stages[lives])


# STEP 5

import random
from hangman_art import stages
from hangman_words import hangman_words


