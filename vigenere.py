class VigenereCipher():
    def __init__(self, key):
        self.key = key

    def expand_key(self, length):
        key_len = len(self.key)
        multiply_factor = length // key_len
        expanded_key = (self.key*multiply_factor) + \
            (self.key[:length % key_len])
        return expanded_key

    def encrypt(self, data):
        key = self.expand_key(len(data))
        ciphertext = b""
        for key_byte, byte in zip(key, data):
            ciphertext += bytes([(byte + key_byte) % 256])
        return ciphertext

    def decrypt(self, data):
        key = self.expand_key(len(data))
        plaintext = b""
        for key_byte, byte in zip(key, data):
            plaintext += bytes([(byte - key_byte) % 256])
        return plaintext
