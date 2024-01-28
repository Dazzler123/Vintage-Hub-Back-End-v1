# Import the cryptography library
from cryptography.fernet import Fernet


def encrypt_password():
    # Generate a Fernet key
    key = Fernet.generate_key()

    # Create a Fernet object with that key
    f = Fernet(key)

    # Input string to be encrypted
    input_string = "Hello World!"

    # Encrypt the string
    encrypted_string = f.encrypt(input_string.encode())

    return encrypted_string

    # # Decrypt the encrypted string
    # decrypted_string = f.decrypt(encrypted_string)
    #
    # # Print the original and decrypted strings
    # print("Original String:", input_string)
    # print("Decrypted String:", decrypted_string.decode())
