# RSA Encrypter & Decrypter

A small Python project to play around with RSA encryption and decryption.  
It can generate public/private keys, encrypt messages, and decrypt ciphertext back to the original text.  

---

## Features
- Auto-generates RSA keys
- Encrypts any text input
- Decrypts using your private key
- Simple command-line interface

---

## How It Works
1. Two random prime numbers are generated (p and q).  
2. Compute n = p * q and φ(n) = (p-1)*(q-1).  
3. Pick a public exponent e coprime with φ(n).  
4. Compute the private key d (modular inverse of e).  
5. Encrypt each character by converting it to ASCII and applying C = P^e mod n.  
6. Decrypt using P = C^d mod n and convert ASCII numbers back to text.  

---

## How to Use
1. Run `main.py`  
2. Choose `E` to encrypt or `D` to decrypt  
3. Follow the prompts for plaintext/ciphertext and keys  


