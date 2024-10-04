import string
import random

def main():
    maxLetters = int(input('How many letters would you like in your password? '))
    maxSimbols = int(input('How many symbols would you like? '))
    maxNumber = int(input('How many numbers would you like? '))

    passwordLetters = []

    for i in range(0,maxLetters + maxSimbols + maxNumber):
        if maxSimbols > 0: 
            passwordLetters.append(random.choice(string.punctuation))
            maxSimbols -= 1
        elif maxNumber > 0:
            passwordLetters.append(random.choice(string.digits))
            maxNumber -= 1
        else:
            passwordLetters.append(random.choice(string.ascii_letters))

    random.shuffle(passwordLetters)

    print(f"\nRandom password: {''.join(passwordLetters)}")


main()
    