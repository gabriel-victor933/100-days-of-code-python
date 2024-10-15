import sys

def main():

    bids = {}

    control = 'yes'

    while control == 'yes':

        name = input('What is your name?: ').capitalize()

        bid = int(input('What is your bid?: $'))

        bids[name] = bid

        control = input("Are there any other bidders? Type 'yes or 'no'.")

        print('\n'*100)
    
    max_name = None

    for key in bids:
        if max_name is None:
            max_name = key
        elif bids[key] > bids[max_name]:
            max_name = key

    print(f"The winner is {max_name} with a bid of ${bids[max_name]}")

main()