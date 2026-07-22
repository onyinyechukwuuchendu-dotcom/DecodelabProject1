def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def main():
    key = 13  # fixed encryption key

    choice = input("Encrypt or decrypt? (e/d): ").lower()

    text = input("Enter your message: ")

    if choice == "e":
        result = encrypt(text, key)
        print("Encrypted:", result)

    elif choice == "d":
        result = decrypt(text, key)
        print("Decrypted:", result)

    else:
        print("Invalid choice.")


main()