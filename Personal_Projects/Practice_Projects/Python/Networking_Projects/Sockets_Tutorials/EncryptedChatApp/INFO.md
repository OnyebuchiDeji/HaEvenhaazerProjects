#   Date Started: Wed-16-Oct-2024


#   Overview
This is a CLI-based Chat App that encrypts the messages it sends over the network.
Hence even if one uses Wireshark to see the packets inn the network traffic being transferred,
they won't be able to understand the encrypted strings


It will mostlikely require installation of a cryptography library
E.g. `pycryptodome`, which is basically the working version of `pycrypto`
But these use Symmetric Encryption.

But in this case, a library called RSA is used.

RSA utilizes assymetric encryption, which makes use of a Public key and a Private (or Secret) key.
Hence it's called 'Assymmetric' because one key is used to encrypt a message and another (the private) to
decrypt that message. 

Hence no one else is meant to know your private key, and it's impossible to derive
the private key from the public key.

`pip install rsa` -- the module for the encryption 

#   Refrences
NeuralNine (2023), "Coding Encrypted Chat in Python".

##  Date Finished: Wed-16-Oct-2024