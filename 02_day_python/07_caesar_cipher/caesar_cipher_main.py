from caesar_cipher_art import logo
# Caesar Cipher Function
def caesar(text, shift, direction):
    result = ""
    alphabet = [chr(i) for i in range(97, 123)]  # a-z

    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            position = alphabet.index(lower_char)
            new_pos = (position + shift) % 26 if direction == "encode" else (position - shift) % 26
            new_char = alphabet[new_pos]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char  # Keep symbols, numbers, and spaces
    print(f"\n🔐 The {direction}d text is: {result}")

# Program Start
print(logo)

should_continue = True
while should_continue:
    direction = input("👉 Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    text = input("✍️ Enter your message:\n")
    shift = int(input("🔁 Enter shift number (1-25):\n")) % 26

    caesar(text=text, shift=shift, direction=direction)

    restart = input("\n🔄 Do you want to go again? Type 'yes' or 'no': ").lower()
    if restart != "yes":
        should_continue = False
        print("👋 Goodbye!")
