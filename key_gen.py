from sympy import randprime
from math import gcd

class Key:
    """
    RSA Key Generator Class
    Generates public and private keys for encryption and decryption.
    """
    def __init__(self):
        # Generate two distinct random primes
        p = randprime(100, 500)
        q = randprime(100, 500)
        while q == p:
            q = randprime(100, 500)

        # Compute modulus n and Euler's totient phi(n)
        self.n = p * q
        self.phi_n = (p - 1) * (q - 1)

        # Choose public exponent e (coprime with phi_n)
        self.e = self.choose_e()

        # Compute private exponent d (modular inverse of e mod phi_n)
        self.d = pow(self.e, -1, self.phi_n)

    def choose_e(self):
        """
        Finds a small integer e that is coprime with phi_n.
        Returns:
            e (int): Public exponent for RSA
        """
        for i in range(2, self.phi_n):
            if gcd(i, self.phi_n) == 1:
                return i




