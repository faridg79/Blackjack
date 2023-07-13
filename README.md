# Blackjack Game

This is a simple command-line implementation of the game Blackjack (also known as 21). The game is played between a player and the computer, and the goal is to get a hand value as close to 21 as possible without exceeding it.

## Instructions

1. Make sure you have Python installed on your computer.
2. Download or clone the `Blackjack` repository.
3. Open a terminal or command prompt and navigate to the project directory.

### Running the Game

1. In the terminal, run the following command to start the game:

   ```bash
   python game.py

1. Follow the prompts on the screen to play the game.
2. The program will display the player's and computer's cards, as well as their current scores.
3. The player can choose to draw another card or stop.
4. Once the player stops or exceeds 21 points, the computer will draw cards automatically until it reaches a score of 17 or more.
5. After the computer finishes drawing cards, the final scores are displayed, and the winner is determined.

# Rules of the Game
+ The game is played with a standard deck of 52 cards.
+ The player's goal is to get a higher score than the computer without exceeding 21 points.
+ Numbered cards (2-10) are worth their face value, face cards (Jack, Queen, and King) are worth 10 points each, and the Ace can be worth either 1 or 11 points.
+ At the beginning of the game, both the player and the computer are dealt two cards.
+ If the player's initial hand is an Ace and a card worth 10 points (10, Jack, Queen, or King), it is called a blackjack and automatically wins the game.
+ The player can choose to draw additional cards ("hit") or stop receiving cards ("stand").
+ If the player's hand exceeds 21 points, they lose the game immediately ("bust").
+ Once the player stands, the computer automatically draws cards until it reaches a score of 17 or more.
+ If the computer's hand exceeds 21 points, it loses the game.
+ If both the player and the computer have the same score, it's a draw.
+ If neither the player nor the computer busts and their scores are different, the one with the higher score wins.

# Code Explanation
The **game.py** file contains the Python code for the Blackjack game. Here's a brief explanation of the main functions:

**deal_card()** : This function randomly selects a card from the deck and returns it.
**calculate_score(cards)** : This function takes a list of cards as input and calculates the total score. It accounts for the value of Ace cards and adjusts the score if necessary.
compare(user_score, computer_score): This function compares the player's score with the computer's score and determines the winner or a draw.
**play_game()** : This function implements the game logic. It initializes the player's and computer's card lists, deals the initial cards, allows the player to draw more cards or stand, lets the computer draw cards, and determines the winner.
The game is played by calling the play_game() function.

**Note** : This implementation uses the random module to simulate card drawing. However, it does not simulate a complete deck or track which cards have been drawn. Thus, the game can draw the same card multiple times, which may not be ideal for a real-world blackjack game.

Feel free to modify and enhance the code to suit your needs and make the game more robust.
