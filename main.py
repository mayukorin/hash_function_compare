from md5 import md5_hash
from sha256 import sha256_hash
from scrypt import scrypt_hash

if __name__ == '__main__':
    print(md5_hash('password'))
    print(sha256_hash('password'))
    print(scrypt_hash('password'))