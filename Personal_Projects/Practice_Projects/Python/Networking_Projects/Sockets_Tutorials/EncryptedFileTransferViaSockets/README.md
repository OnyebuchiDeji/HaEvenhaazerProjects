#   Date Started: Wed-16-Oct-2024


#   Overview
This demonstrates a symmetric encryption a type.
Symmetric means the same key is uesd for encryption and decryption.
In constrast is a technique like RSA that uses Assymetric encryption, where the public key
is used for encryption and another key, the private one is used for decryption


By encryption, when one uses wirreshark to look at the packets being transmitted over the network
they won't be able to see the actual string, they will see the encrypted bytes


#   Libraries
1.  pip install pycrypto
    But pycrypto was not working, because the repo has not been maintained.
    So rather do `pip install pycryptodome`
2.  pip install tqdm, for command line progress bars


#   Reference
NeuralNine (2023), "Encrypted File Transfer via Sockets in Python"

#   Done: Wed-16-Oct-2024