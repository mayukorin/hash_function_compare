import hashlib

def calc_md5_hash(plain_text):
    return hashlib.md5(plain_text.encode()).hexdigest()