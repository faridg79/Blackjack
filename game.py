import random

cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    card_values = {
        'Ace': 11,'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10
    }

    if sum(card_values[card] for card in cards) == 21 and len(cards) == 2:
        return 0

    if 'Ace' in cards and sum(card_values[card] for card in cards) > 21:
        for i in range(len(cards)):
            if cards[i] == 'Ace':
                cards[i] = '1'
                break

    return sum(card_values[card] for card in cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose! You have exceeded 21 points."

    if user_score == computer_score:
        return "It's a draw!"

    if user_score == 0:
        return "You win! Player has blackjack."

    if computer_score == 0:
        return "You lose! Computer has blackjack."

    if user_score > 21:
        return "You lose! You have exceeded 21 points."

    if computer_score > 21:
        return "You win! Computer has exceeded 21 points."

    if user_score > computer_score:
        return "You win!"

    return "You lose!"


def play_game():
    print("Welcome to Blackjack!")

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_continue = input("Do you want to draw another card? 'y' or 'n': ")
            if user_should_continue == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's cards: {computer_cards}, current score: {computer_score}")
    print(compare(user_score, computer_score))


play_game()
