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

# -----------------------------------------------------------------
# Second variant of the blackjacj game

import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, result: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


blackjack()