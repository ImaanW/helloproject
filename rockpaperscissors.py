#Let's play! You have to return which player won! In case of a draw return Draw!.

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif(p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'rock' and p2 == 'scissors'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'


# demostrates
# if player one variable is == to player two then  RETURN it is a draw

# elif _ (if false cont) is these combinations occur - all combinations that player 1 wins
# return play won wins

# else/otherwise return player 2 won!