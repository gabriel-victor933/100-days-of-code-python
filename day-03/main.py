def main():

    print('Welcome to Treasure Island. Your mission is to find the treasure.')

    direction = input("left or right? ")

    if direction != 'left':
        print('Fall into a hole. Game Over.')
        return
    
    action = input("swim or wait? ")

    if action != 'wait':
        print('Attacked by trout. Game Over.')
        return
    
    door = input("Which door? ")

    if door == 'red':
        print('Burned by fire.Game Over.')
    elif door == 'yellow':
        print('You Win!')
    elif door == 'blue':
        print('Eaten by beasts. Game Over.')
    else:
        print('Game Over.')


main()