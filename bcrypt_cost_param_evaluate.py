from bcrypt_hash import calc_bcrypt_hash

if __name__ == '__main__':

    # hash計算にかかる時間を測定
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "123abc", "password1", "12345", "abcdef"]

    for cost in [12, 13, 14, 15, 16, 17, 18, 19, 20]:
        scrypt_avg_time = 0
        for password in common_passwords:
            scrypt_avg_time += calc_bcrypt_hash(password, cost=cost)[1]
        print('scrypt average time (cost={}): {} s'.format(cost, scrypt_avg_time/len(common_passwords)))
