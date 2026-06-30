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
    if winning_moves[player] == computer:
        return "draw"
    
    return computer

def playgame():
    print(" Enter to the rock , paper  , scissors game .")
    
    while True:
        player = input(" please select one from (rock , paper , scissors):").strip().lower()
        
        if player not in CHOICES:
            return " invalid syntax please enter valid choices"
        
        computer = get_computer_choices
        result  = decide_winner(player , computer)
           
        
        print(f"your choices:{player}") 
        print(f"computer choice:{computer}")   
        
        if result == player:
            print("you win the game")
            
        if result == computer:
            print(" computer win ") 
            
        if result == draw :
            print(" match tied")
            
        play_again = input(" DO YOU WANT TO PLAY AGIAN : YES /NO").strip().lower()
            
        if play_again != 'yes':
            print(" THANKS FOR PLAYING")
            break
        
playgame()