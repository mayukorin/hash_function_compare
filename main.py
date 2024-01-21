from md5 import md5_hash
from sha256 import sha256_hash

if __name__ == '__main__':
    print(md5_hash('password'))
    print(sha256_hash('password'))