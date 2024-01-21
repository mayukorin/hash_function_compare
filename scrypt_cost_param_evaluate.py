from scrypt_hash import calc_scrypt_hash

if __name__ == '__main__':

    # hash計算にかかる時間を測定
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "123abc", "password1", "12345", "abcdef"]

    for cost_factor in [16384, 32768]:
        scrypt_avg_time = 0
        for password in common_passwords:
            scrypt_avg_time += calc_scrypt_hash(password, cost_factor=cost_factor)[1]
        print('scrypt average time (cost_factor={}): {} s'.format(cost_factor, scrypt_avg_time/len(common_passwords)))
