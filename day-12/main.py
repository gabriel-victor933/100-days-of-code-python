import random

def main(): 
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")

    random_int = random.randint(0,100)
    
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    
    if difficulty.lower() == 'easy':
        number_attempts = 10
    else:
        number_attempts = 5

    
    while number_attempts > 0:
        print(f'You have {number_attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))

        if guess == random_int:
            print(f'You got it! The answer was {guess}.')
            return
        elif guess > random_int:
            print('Too high.')
        else:
            print('Too low.')     
        
        number_attempts -= 1


main()