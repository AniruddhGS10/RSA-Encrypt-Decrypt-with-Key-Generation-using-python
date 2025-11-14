from key_gen import Key

class Encrypt(Key):
    def __init__(self):
        super().__init__()  # Initialize Key class to generate n, phi_n, e, d

    def encrypt(self, plaintext):
        """
        Encrypts a plaintext string using RSA algorithm.

        Steps:
        1. Convert each character to its ASCII value.
        2. Encrypt each ASCII value using C = P^e mod n.
        3. Return the list of encrypted numbers as ciphertext.
        """

        # Convert each character in plaintext to its ASCII number
        ascii_values = [ord(char) for char in plaintext]

        # Encrypt each ASCII number using the RSA public key (e, n)
        ciphertext = [pow(num, self.e, self.n) for num in ascii_values]

        # Return the ciphertext as a list of integers
        return ciphertext


