import os

# lets create a module to encrypt and decrypt a file

print(os.getcwd())

def encrypt(file):
    encoded_file = os.fsencode(file)
    return encoded_file
    #encrypt a file
    # return said ecrypt

def decrypt(file):
    decoded_file = os.fsdecode(file)
    return decoded_file
    # decrypt a file
    # return decrypted file