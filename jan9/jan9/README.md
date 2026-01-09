📌 Project Overview

This project is a Rock Paper Scissors game implemented in Python using Object-Oriented Programming (OOP) concepts.
The program allows a player to play multiple rounds against the computer, keeps track of scores, and displays the final scoreboard.

In the program a class is created 

🔹 Class: RPSGame

The class represents the Rock Paper Scissors game.

Attributes:

*player_name – Name of the player

*player_score – Player’s score

*computer_score – Computer’s score

*Constructor (__init__)

*Saves the player name

*Initializes both scores to 0

🔹 Methods
1. play_round()

-Takes the player’s move

-Generates the computer’s move randomly

-Decides the winner using if / elif / else

-Updates the scores

-Displays the result of the round

2.show_score()

-Displays the final scoreboard after all rounds are completed


▶️ How the Game Runs

1.Ask the user for their name

2.Ask how many rounds they want to play

3.Run play_round() inside a loop for given rounds

4.Call show_score() at the end to display final scores
