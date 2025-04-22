"""
    Can also generate the same key using the same salt and password
    to be able to decrypt the binary decrypted file.
"""

from Crypto.Random import get_random_bytes
"""The PBKDF2 is an algorithm for encryption that makes brute force break-ins more difficult"""
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


salt = b""

with open("salt.bin", "rb") as f:
    salt = f.read()

pwd = "MySecretPWD:BEANS"

#   Generates the same key as in `main.py`
key = PBKDF2(pwd, salt, dkLen=32)


#   Load Encrypted Message
with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    decrypted_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypted_data), AES.block_size)
print(original)