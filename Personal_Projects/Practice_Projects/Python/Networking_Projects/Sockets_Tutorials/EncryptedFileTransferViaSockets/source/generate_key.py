"""
    This just demonstrates the creation of the script.
    The Key must have 16 bytes.
    The salt text (or nonce text) also should have 16 bytes
"""

from Crypto.Cipher import AES   #   Advanced Encryption Standard


key = b"TheEvenhaazerKey"
nonce = b"TheEvenhaazerNce"


cipher = AES.new(key, AES.MODE_EAX, nonce)
#   This uses the text to encrypt the key
ciphertext = cipher.encrypt(b"ThisSaysYoWorld!")

print(ciphertext)

#   Note it's the same as the above -- the same key
cipher_to_decrypt = AES.new(key, AES.MODE_EAX, nonce)
print(cipher.decrypt(ciphertext))