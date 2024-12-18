# -------------------------------------------------------
# First variant of Blackjack game

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add(hand):
    return sum(hand)


def blackjack():
    print(logo)
    user_hand = random.sample(cards, 2)
    computers_hand = random.sample(cards, 2)

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "y":
        user_score = add(user_hand)
        computer_score = add(computers_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computers_hand[0]}")

    else:
        print("Maybe next time!")

    choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if choice == "y":
        user_hand = random.sample(cards, 1) + user_hand
        user_score = add(user_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's final hand: {computers_hand}, final score {computer_score}")
        if user_score > 21:
            print("You lose")
        elif user_score > computer_score:
            print("You win")
        elif computer_score > user_score:
            print("You lose")
    else:
        print(f"Your cards: {user_hand}, current score: {add(user_hand)}")
        print(f"Computer's final hand: {computers_hand}, final score {add(computers_hand)}")
        if user_score > 21:
            print("You lose")
        elif user_score > computer_score:
            print("You win")
        elif computer_score > user_score:
            print("You lose")

    final_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if final_choice == "y":
        print("\n" * 20)
        blackjack()
    else:
        print("Have a nice day!")


blackjack()