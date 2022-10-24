import random
from time import sleep
def rps():
    game_runs = int(input('Enter the number of times you wish to play this game in figures: '))
    runtimes = []

    while game_runs > 0:
        runtimes.append(game_runs)
        game_runs -= 1

    for number in runtimes:
        player_input = input('Enter r, p or s for Rock, Paper and Scissors:')
        possible_actions = ['r', 'p', 's']
        computer_input = random.choice(possible_actions)

        if player_input in possible_actions:
            print(f'You chose {player_input} and the computer chose {computer_input}')
            
            if player_input == computer_input:
                print(f"Both players chose {computer_input}, it's a tie")
            elif player_input == 'r':
                if computer_input == 's':
                    print('Rock smashes scissors, You win!')
                else:
                    print('Paper covers rock, Computer wins')
            elif player_input == 'p':
                if computer_input == 'r':
                    print('Paper covers rock, You win!')
                else:
                    print('Scissors cuts paper, Computer wins')
            elif player_input == 's':
                if computer_input == 'p':
                    print('Scissors cuts paper, You win!')
                else:
                    print('Rock smashes scissors, Computer wins')
            sleep(1)             
        else:
            raise ValueError('Invalid entry')

rps()