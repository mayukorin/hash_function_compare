import hashlib
import time

def calc_md5_hash(plain_text):
    start_time = time.time()
    hash = hashlib.md5(plain_text.encode()).hexdigest()
    end_time = time.time()
    return hash, end_time-start_time