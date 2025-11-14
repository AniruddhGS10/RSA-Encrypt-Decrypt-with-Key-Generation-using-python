from key_gen import Key

class Decrypt(Key):
    def __init__(self, d, n):
        """
        Initialize the Decrypt class with user-provided RSA private key.
        :param d: Private exponent
        :param n: Modulus
        """
        super().__init__()  # Initialize Key class (optional here, kept for consistency)
        self.d = d
        self.n = n

    def decrypt(self, ciphertext):
        """
        Decrypts a list of integers (ciphertext) using RSA algorithm.

        Steps:
        1. Apply modular exponentiation: P = C^d mod n
        2. Convert resulting numbers (ASCII) back to characters
        3. Join characters to get the original plaintext string
        """
        # Apply RSA decryption on each number
        ascii_values = [pow(c, self.d, self.n) for c in ciphertext]

        # Convert ASCII values back to string
        plaintext = ''.join([chr(num) for num in ascii_values])

        # Return the decrypted plaintext
        return plaintext



