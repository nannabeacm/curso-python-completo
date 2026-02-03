### 93
print("\n===== 93 ======\n")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("=== ENCRYPTOR ===")
text = input("Type your message: ").lower()
shift = int(input("Shift every letter by: "))

def encrypt(text, shift):
    output_text = ""
    for letter in text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift
            shifted_position = shifted_position % len(alphabet)
            output_text = output_text + alphabet[shifted_position]
        else:
            output_text += letter       
    return output_text

encrypted_text = encrypt(text, shift)
print(f"Encrypted message: {encrypted_text}")