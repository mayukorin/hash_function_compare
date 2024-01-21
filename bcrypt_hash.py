import bcrypt
import time

def calc_bcrypt_hash(plain_text):
    start_time = time.time()
    cost = 12
    hash = bcrypt.hashpw(plain_text.encode(), bcrypt.gensalt(rounds=cost)).hex()
    end_time = time.time()
    return hash, end_time-start_time