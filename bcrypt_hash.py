import bcrypt

def calc_bcrypt_hash(plain_text):
    cost = 12
    return bcrypt.hashpw(plain_text.encode(), bcrypt.gensalt(rounds=cost)).hex()