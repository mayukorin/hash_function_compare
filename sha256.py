import hashlib

def sha256_hash(plain_text):
    return hashlib.sha256(plain_text.encode()).hexdigest()