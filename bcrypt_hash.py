import bcrypt
import time

def calc_bcrypt_hash(plain_text, cost):
    start_time = time.time()
    hash = bcrypt.hashpw(plain_text.encode(), bcrypt.gensalt(rounds=cost)).hex()
    end_time = time.time()
    return hash, end_time-start_time