# encryption.py
from cryptography.fernet import Fernet

class CryptoHandler:
    def __init__(self):
        # Generate a new encryption key
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def encrypt(self, plaintext):
        """
        Encrypts the given plaintext using the Fernet encryption.
        
        Args:
            plaintext (str): The plaintext message to encrypt.
        
        Returns:
            str: The encrypted message in string format.
        """
        # Encrypt the plaintext and return it as a string
        encrypted_message = self.cipher_suite.encrypt(plaintext.encode())
        return encrypted_message.decode()
    
    def decrypt(self, ciphertext):
        """
        Decrypts the given ciphertext using the Fernet encryption.
        
        Args:
            ciphertext (str): The encrypted message to decrypt.
        
        Returns:
            str: The decrypted plaintext message.
        """
        # Decrypt the ciphertext and return the plaintext
        decrypted_message = self.cipher_suite.decrypt(ciphertext.encode())
        return decrypted_message.decode()
    
    def get_key(self):
        """
        Returns the current encryption key.
        
        Returns:
            str: The encryption key in string format.
        """
        return self.key.decode()

    def set_key(self, key):
        """
        Sets a new encryption key for the cipher suite.
        
        Args:
            key (str): The new encryption key to set.
        """
        self.key = key.encode()
        self.cipher_suite = Fernet(self.key)
