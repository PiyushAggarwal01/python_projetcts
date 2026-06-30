import random
CHOICES = ['rock', 'paper','scissors']
def get_computer_choices():
    choice =random.choice(CHOICES)
    
def decide_winner(player , computer):
    if player == computer:
        return "draw"
    winning_moves ={
        "rock" : "scissors",
        "paper": "rock",
        "scissors":"paper"
        
    }
        