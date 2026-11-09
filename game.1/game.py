import random


# Define your own functions here.
def random_strategy():
    return random.randint(0, 2)
def assign(player):
    if player == 0:
        player = "ROCK"
    if player ==1:
        player = "PAPER"
    if player == 2:
        player = "SCISSORS"
    return player
def beat(player_one, player_two):
    if player_one == 0:
        if player_two == 0:
            winner = 0
        if player_two == 1:
            winner = 2
        if player_two == 2:
            winner = 1
    if player_one == 1:
        if player_two == 0:
            winner = 1
        if player_two == 1:
            winner = 0
        if player_two == 2:
            winner = 2
    if player_one == 2:
        if player_two == 0:
            winner = 2
        if player_two == 1:
            winner = 1
        if player_two == 2:
            winner = 0
    return winner


    


def main():
    # Build your playable game here, calling your functions.
    p1_count = 0
    p2_count = 0
    for i in range(0, 2):
        player_one = random_strategy()
        player_two = random_strategy()
        round_winner = beat(player_one, player_two)
        if round_winner == 0:
            round_winner = "TIE"
        elif round_winner == 1:
            round_winner = "PLAYER 1 WINS" 
        else:
            round_winner = "PLAYER 2 WINS"            
        

    player_one = "Player 1", assign(player_one)
    player_two = "Player 2", assign(player_two)
   
    
    print(round_winner)
    print(player_one)
    print(player_two)

    



if __name__ == "__main__":
    main()
