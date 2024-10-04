alphabet = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for letter in original_text:

        if letter not in alphabet:
            encrypted_text += letter
            continue

        index = alphabet.index(letter) + shift_amount
        index %= len(alphabet)
        encrypted_text += alphabet[index]

    print(encrypted_text)

def decrypt(encrypted_text, shift_amount):
    original_text = ''
    for letter in encrypted_text:

        if letter not in alphabet:
            original_text += letter
            continue

        index = alphabet.index(letter) - shift_amount
        index %= len(alphabet)
        original_text += alphabet[index]

    print(original_text)

response = 'yes'
while response == 'yes':
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    message = input("Type your message: ")
    shift_number = int(input("Type the shift number: "))

    if action == "encode":
        encrypt(message,shift_number)
    else:
        decrypt(message,shift_number)

    response = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")