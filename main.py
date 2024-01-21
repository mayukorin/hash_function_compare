from md5_hash import calc_md5_hash
from sha256_hash import calc_sha256_hash
from scrypt_hash import calc_scrypt_hash
from bcrypt_hash import calc_bcrypt_hash


if __name__ == '__main__':
    # 表示される hash値確認
    md5_hash, _ = calc_md5_hash('password')
    print('md5_hash:{}'.format(md5_hash))

    sha256_hash, _ = calc_sha256_hash('password')
    print('sha256_hash:{}'.format(sha256_hash))

    scrypt_hash, _ = calc_scrypt_hash('password')
    print('scrypt_hash:{}'.format(scrypt_hash))

    bcrypt_hash, _ = calc_bcrypt_hash('password')
    print('bcrypt_hash:{}'.format(bcrypt_hash))

    # hash計算にかかる時間を測定
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "123abc", "password1", "12345", "abcdef"]
    md5_avg_time = 0
    sha256_avg_time = 0
    scrypt_avg_time = 0
    bcrypt_avg_time = 0

    for password in common_passwords:
        md5_avg_time += calc_md5_hash(password)[1]
        sha256_avg_time += calc_sha256_hash(password)[1]
        scrypt_avg_time += calc_scrypt_hash(password)[1]
        bcrypt_avg_time += calc_bcrypt_hash(password)[1]

    print('md5 average time: {} s, sha256 average time: {} s, scrypt average time: {} s, bcrypt average time: {} s'.format(md5_avg_time/len(common_passwords), sha256_avg_time/len(common_passwords), scrypt_avg_time/len(common_passwords), bcrypt_avg_time/len(common_passwords)))
