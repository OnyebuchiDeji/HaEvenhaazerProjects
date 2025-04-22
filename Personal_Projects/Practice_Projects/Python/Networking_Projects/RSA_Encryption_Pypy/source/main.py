
"""
    The message encrypted by the Public Key can only be decrypted with the private key.
    Also, one can sign a document with a private key, making it authentic, and the public key
    will verify this signature.
    the public key will only be able to verify the signature if it was signed by the private key
    
    ELAB:
        For the latter, the Public key encrypts messages from the Public sent to me, to ensure that
        their data to me is not seen by anyone.
        Another use, for me to send messages to the public so that they know that it's from me, I
        add a signature using my private key, and they use the public key they have to verify
        the signed message, that it indeed is from me.
        Signing using the private key does not encrypt the message; it just verifies that it's from me.
"""

import rsa
import os


def write_keys():
    """
        The longer the string, the more bytes are required, lest it prints this error:
        raise OverflowError(
            OverflowError: 127 bytes needed for message, but there is only space for 117
    
    """
    public_key, private_key = rsa.newkeys(2048) #   was 1024

    #   It's the public key that one would make available to the public for them to send
    #   messages to the owner to ensure only you (the owner) can see the public's messages
    with open("public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


def read_keys():
    with open("public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    
    with open("private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    
    return public_key, private_key
    

def write_encrypted_msg():
    message = "Yo! Yo! It's Eben. I am strong, and the Word of God abides in me. Also, I like pleasant things and love my family and brethren!"
    public_key = read_keys()[0]
    encrypted_msg = rsa.encrypt(message.encode(), public_key)
    
    #   write encrypted message
    with open("encrypted_message.txt", "wb") as f:
        f.write(encrypted_msg)

def read_encrypted_msg():
    private_key = read_keys()[1]
    with open("encrypted_message.txt", "rb") as f:
        msg = rsa.decrypt(f.read(), private_key).decode()
    return msg

def encrypting_message():
    write_keys()
    write_encrypted_msg()
    print(f"\nThe Message that was encrypted, now decrypted:\n{read_encrypted_msg()}\n")


def signing_message():
    """
        The goal is to know if the below message is actually from me using the signature

        If the message used to create the signature is changed, or the keys are changed
        and these changed keys and or message are used in the rsa.verify(), it will cause an error. 

        Try Changing this first message, or make new keys
    """
    message = "I am like cheese balls, they are my favorite snacks"

    signature = rsa.sign(message.encode(), read_keys()[1], "SHA-256")

    # print(__file__)
    pathToCheck = os.path.join(os.path.dirname(__file__), "..", "signature.txt")
    # print(pathToCheck)
    if not os.path.exists(pathToCheck):
        print("Doesn't yet exist")
        with open("signature.txt", "wb") as f:
            f.write(signature)
        
    with open("signature.txt", "rb") as f:
        signature = f.read()

    
    """
        rsa.verify returns a string; the last arg is the public key!
        it returns SHA-256, which means the message is authentic.
        print(rsa.verify(message.encode(), signature, read_keys()[0]))
    
    """

    """
        Doesn't work!
        Demonstrating using different public keys to verify signature
        already created with prior private key
    
    """
    new_pub_key, new_priv_key = rsa.newkeys(2048)
    print(rsa.verify(message.encode(), signature, new_pub_key))



def main():
    signing_message()

    

    


    


if __name__ == "__main__":
    main()