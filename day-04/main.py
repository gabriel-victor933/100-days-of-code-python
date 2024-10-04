import random
import my_module

def main():
    
    possibilities = ['Rock', 'Paper', 'Scissors']

    choosed = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

    ranNumber = random.randint(0,2)

    yourChoice = possibilities[choosed]
    computerChoice = possibilities[ranNumber]

    print(f"you choose: {yourChoice}")
    print(f"computer choose: {computerChoice}")

    if yourChoice == computerChoice:
        print('Its a Draw')
    else: 
        if yourChoice == 'Rock':
            if computerChoice == 'Paper':
                print('You lose!')
            else:
                print('You Win!')

        if yourChoice == 'Paper':
            if computerChoice == 'Scissors':
                print('You lose!')
            else:
                print('You Win!')

        if yourChoice == 'Scissors':
            if computerChoice == 'Rock':
                print('You lose!')
            else:
                print('You Win!')
main()