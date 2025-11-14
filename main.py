from encrypt import Encrypt
from decrypt import Decrypt

# Create an Encrypt object (automatically generates keys)
encryptor = Encrypt()

# Welcome message
print("=== Welcome to RSA Encrypter and Decrypter ===")

# Ask the user what they want to do
user_choice = input("Do you want to Encrypt or Decrypt? (Type 'E' for encryption, 'D' for decryption): ").upper()

if user_choice == "E":
    # Ask for plaintext input
    plaintext = input("Please enter the plaintext you want to encrypt: ")

    # Encrypt the message
    ciphertext = encryptor.encrypt(plaintext)

    # Display the results
    print("\nEncrypted Ciphertext:", ciphertext)
    print("Public key (e, n):", (encryptor.e, encryptor.n))
    print("Private key (d, n):", (encryptor.d, encryptor.n))  # displayed for demonstration

elif user_choice == "D":
    # Ask the user to input the ciphertext (numbers separated by spaces)
    ciphertext_str = input("Enter the ciphertext (numbers separated by spaces): ")
    # Convert string input into a list of integers
    ciphertext = list(map(int, ciphertext_str.strip().split()))

    # Ask the user to provide their private key
    d = int(input("Enter your private exponent 'd': "))
    n = int(input("Enter your modulus 'n': "))

    # Create a Decrypt object with provided keys
    decryptor = Decrypt(d, n)

    # Decrypt the ciphertext
    plaintext = decryptor.decrypt(ciphertext)
    print("Decrypted text:", plaintext)

else:
    print("Invalid choice. Please type 'E' for encryption or 'D' for decryption.")




