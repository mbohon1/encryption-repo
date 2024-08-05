
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save the key to a file
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Encrypt a message
message = b'This is a secret message'
cipher_text = cipher_suite.encrypt(message)

# Save the encrypted message to a file
with open('encrypted_message.txt', 'wb') as encrypted_file:
    encrypted_file.write(cipher_text)

print('Encryption complete. Key and encrypted message saved to files.')
