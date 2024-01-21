import hashlib
import time

def calc_sha256_hash(plain_text):
    start_time = time.time()
    hash = hashlib.sha256(plain_text.encode()).hexdigest()
    end_time = time.time()
    return hash, end_time-start_time