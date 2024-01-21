import pyscrypt
import os
import time

def calc_scrypt_hash(plain_text, cost_factor):
    start_time = time.time()
    salt = os.urandom(16)
    hash = pyscrypt.hash(password=plain_text.encode(), salt=salt, N=cost_factor, r=8, p=1, dkLen=32).hex()
    end_time = time.time()
    return hash, end_time-start_time