from md5_hash import calc_md5_hash
from sha256_hash import calc_sha256_hash
from scrypt_hash import calc_scrypt_hash
from bcrypt_hash import calc_bcrypt_hash


if __name__ == '__main__':
    print(calc_md5_hash('password'))
    print(calc_sha256_hash('password'))
    print(calc_scrypt_hash('password'))
    print(calc_bcrypt_hash('password'))