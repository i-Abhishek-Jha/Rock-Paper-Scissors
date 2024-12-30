import random

def play():
    user = input("Choose one: 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    while user not in ['r', 'p', 's']:
        print("Invalid Input\nChoose one: 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    computer = random.choice(['r', 'p', 's'])
    
    choice = {
        'r' : 'rock',
        'p' : 'paper',
        's' : 'scissors'
    }

    print(f"You chose {choice[user]}\nComputer chose {choice[computer]}")
    
    if user == computer:
        return "It's a draw!"
    
    if is_win(user, computer):
        return 'You win!'
    
    return 'You lose!'
     
    
# Winning conditions: r > s, p > r, s > p
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
       (player == 'p' and opponent == 'r') or \
       (player == 's' and opponent == 'p'):
        return True

# Main game loop
if __name__ == "__main__":
    while True:
        print(play())

        replay = input("Do you want to play again? (y: yes/n: no): ").lower()
        if replay not in  ['yes', 'y']:
            print("Thanks for playing!")
            break



