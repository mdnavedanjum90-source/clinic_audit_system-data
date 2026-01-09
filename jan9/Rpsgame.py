# Importing the random package to generate the computer's move
import random

#Defining class 'RpsGame' to represent the game of "Rock, Paper and Scissors"
class RpsGame:
    
    #Defining _init_ method to store player name, player score and computer score
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0
        self.computer_score = 0
        
    # Defining play_round method to
    def play_round(self):
        choices = ["rock", "paper", "scissors"]
        player_move = input("Enter your move: (rock/paper/scissors) ").lower()
        computer_move = random.choice(choices)
        print(f"Computer chose {computer_move}")
    
        # Checking the conditions for the RPS game
        if(computer_move == player_move):
            print("RESULT : It's a draw!")
        else:
            if(computer_move=="rock" and player_move=="paper"):
                print("RESULT : You Win!")
                self.player_score += 1 # Increasing the player score by 1 when player wins
            elif(computer_move=="paper" and player_move=="scissors"):
                print("RESULT : You Win!")
                self.player_score += 1 # Increasing the player score by 1 when player wins
            elif(computer_move=="scissors" and player_move=="rock"):
                print("RESULT : You Win!")
                self.player_score += 1# Increasing the player score by 1 when player wins
            else:
                print("RESULT : You Lose!")
                self.computer_score += 1 # Increasing the computer score by 1 when computer wins
                
     
     # Defining the show_score method to print the final scores           
    def show_score(self):
        print("\n---SCOREBOARD---")
        print(f"{self.player_name} : {self.player_score}")
        print(f"Computer : {self.computer_score}")
        
        
        
#  Running the game 
player_name = input("Enter player name: ")
rounds = int(input("Enter the number of rounds: "))

game = RpsGame(player_name)

i = 1
for i in range(rounds):
    game.play_round()
    
    
    
game.show_score()    
