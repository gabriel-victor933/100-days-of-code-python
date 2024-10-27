import pandas

data = pandas.read_csv("day-26/nato_phonetic_alphabet.csv")

decoded = {row.letter:row.code for (index,row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()

    decoded_list = [decoded[letter] for letter in word]
    
    print(decoded_list)
    print('\n')