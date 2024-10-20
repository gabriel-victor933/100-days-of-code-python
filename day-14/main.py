import random

data = [
    {
        'name': 'Neymar',
        'follower_count': 100
    },
    {
        'name': 'Kanye West',
        'follower_count': 140
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 230
    },
    {
        'name': 'Tom Cruise',
        'follower_count': 120
    },
    {
        'name': 'Adam Sandler',
        'follower_count': 80
    },
    {
        'name': 'Lebron',
        'follower_count': 110
    },
    {
        'name': 'Brad Pitt',
        'follower_count': 134
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 79
    },
]

def main():
    
    score = 0
    one = data.pop(random.randint(0,len(data) - 1))

    while len(data) > 0:
        two = data.pop(random.randint(0,len(data) - 1))
        
        print(f'Compare A: {one["name"]}')
        print(f'Compare B: {two["name"]}')

        letter = input('Who has more followers? Type \'A\' or \'B\':\ ')

        right = 'A' if one['follower_count'] >= two['follower_count'] else 'B'

        if letter == right:
            score += 1
            one = two
            print('\n'*50)
            print(f'You\'re right! Current score: {score}.')
        else: 
            print(f'Sorry, that\'s wrong. Final score: {score}')
            return

    print(f'You you won! Final score: {score}.')

main()