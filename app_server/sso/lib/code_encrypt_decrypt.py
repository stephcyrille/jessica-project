from cryptography.fernet import Fernet


def encrypt_message(message, key):
    """
    Encrypts a message
    """
    key = key
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message


def decrypt_message(encrypted_message, key):
    """
    Decrypts an encrypted message
    """
    key = key
    f = Fernet(key)
    val = encrypted_message.encode()
    decrypted_message = f.decrypt(val)
    return decrypted_message