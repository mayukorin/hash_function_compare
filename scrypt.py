import pyscrypt
import os

def scrypt_hash(plain_text):
    salt = os.urandom(16)
    return pyscrypt.hash(password=plain_text.encode(), salt=salt, N=8192, r=8, p=1, dkLen=32).hex()