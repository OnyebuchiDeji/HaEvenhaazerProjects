"""
    This shows that the key can be exported and imported here, and used to load and decrypt the encrypted
    message
"""

from Crypto.Random import get_random_bytes
"""The PBKDF2 is an algorithm for encryption that makes brute force break-ins more difficult"""
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad



#   Load Key
with open("key.bin", "rb") as f:
    key = f.read()

#   Load Encrypted Message
with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    decrypted_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypted_data), AES.block_size)
print(original)