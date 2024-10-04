import random

words = ["gabriel","victor","alves","santana"]

MAX_ATTEMPS = 6


def main():
    attempts = 0
    word = list(random.choice(words))
    blankSpaces = []
    chosen = []

    for i in range(0,len(word)):
        blankSpaces.append("_")

    while attempts <= MAX_ATTEMPS:
        print(f'Word to guess: {"".join(blankSpaces)}')
        letter = input("Guess a letter: ").lower()

        if letter in chosen:
            print(f'The letter {letter} has already been chosen\n')
            continue

        if letter in word:
            for i in range(0,len(word)):
                if letter == word[i]:
                    blankSpaces[i] = letter

            print(f'{"".join(blankSpaces)}\n')

            if "_" not in blankSpaces:
                print("You Win!!!")
                return

        else:
            print(f"You guessed {letter}, that's not in the word. You lose a life.\n")
            attempts += 1

        chosen.append(letter)

    print(f'IT WAS {"".join(word)}! YOU LOSE')

main()  