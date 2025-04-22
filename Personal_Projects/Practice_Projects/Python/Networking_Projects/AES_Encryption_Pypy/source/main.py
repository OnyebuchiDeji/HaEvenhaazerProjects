"""
    So Simple!
"""

from Crypto.Random import get_random_bytes
"""The PBKDF2 is an algorithm for encryption that makes brute force break-ins more difficult"""
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


#   Will be used as the salt for the actual generated key
prior_simple_key = get_random_bytes(32)
# print(prior_simple_key)

with open ("salt.bin", "wb") as f:
    f.write(prior_simple_key)



salt = prior_simple_key
pwd = "MySecretPWD:BEANS"

#   Note how the password is used to create this key
key = PBKDF2(pwd, salt, dkLen=32)
print("Key: ", key)

msg = b"Yo! Greetings from Deji! :)"

#   cipher used to encrypt the message
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(msg, AES.block_size))

print("Ciphered Data: ", ciphered_data)

with open("encrypted.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    decrypted_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv= iv)
og = unpad(cipher.decrypt(decrypted_data), AES.block_size)
print(og)

"""Can also export the key and use it for decryption in another file"""

with open("key.bin", "wb") as f:
    f.write(key)