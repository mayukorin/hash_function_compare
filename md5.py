import hashlib

def md5_hash(plain_text):
    return hashlib.md5(plain_text.encode()).hexdigest()