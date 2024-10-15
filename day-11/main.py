import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def swapEleven(arr):
    if sum(arr) > 21 and 11 in arr: 
        arr.remove(11)
        arr.append(1)

def printGame(my_cards,dealer_cards):
    print(f"\nYour cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {dealer_cards}")

def pickCard():
    return random.choice(cards)

def main():
    
    
    while True: 
        control = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if control == 'n':
            break

        my_cards = []
        dealer_cards = []

        my_cards.append(11)
        dealer_cards.append(pickCard())
        my_cards.append(pickCard())

        printGame(my_cards,dealer_cards)

        while True:
            if sum(my_cards) > 21:
                print('End Game! You Lose!\n\n')
                break

            elif sum(my_cards) == 21:
                print('Congratulations you won!\n\n')
                break

            another = input("Type 'y' to get another card, type 'n' to pass: ")

            if another == 'n':
                while sum(dealer_cards) < 21 and sum(dealer_cards) < sum(my_cards):
                    dealer_cards.append(pickCard())
                    swapEleven(dealer_cards)
                
                printGame(my_cards,dealer_cards)

                if sum(dealer_cards) > 21:
                    print('Congratulations you won!\n\n')
                elif sum(dealer_cards) == 21:
                    print('End Game! You Lose! Dealers got 21!\n\n')
                elif sum(dealer_cards) > sum(my_cards):
                    print('End Game! You Lose! Dealers got more!\n\n')
                elif sum(dealer_cards) == sum(my_cards):
                    print('End Game! it is a draw\n\n')
                else: 
                    print('Congratulations you won!\n\n')

                break

            my_cards.append(pickCard())

            swapEleven(my_cards)

            printGame(my_cards,dealer_cards)



main()