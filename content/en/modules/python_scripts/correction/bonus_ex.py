import argparse

def base_k(n, k):
    assert 0 < k and k < 10
    r = 0
    p = 0
    while n > 0:
        r += 10**p * (n % k)
        p += 1
        n = n // k
    return r

def base_10(n, k):
    r = 0
    digits = [int(i) for i in str(n)]
    digits.reverse()
    for i, d in enumerate(digits):
        r += k**i * d
    return r


def encrypt_letter(msg, key):
    k = 5 + ord(key) % 5
    enc_id = base_k(ord(msg)+ord(key), k) % 1114111
    return chr(enc_id)


def decrypt_letter(msg, key):
    k = 5 + ord(key) % 5
    dec_id = (1114111 + base_10(ord(msg), k) - ord(key)) % 1114111
    return chr(dec_id)


def process_message(message, keys, encrypt):
    while len(keys) < len(message):
        keys += keys
    returned_message = ""

    for i, letter in enumerate(message):
        returned_message += encrypt_letter(letter, keys[i]) if encrypt else decrypt_letter(letter, keys[i])

    return returned_message

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str)
    parser.add_argument("--key", type=str)
    parser.add_argument("--mode", type=str, choices=["enc", "dec"])
    args = parser.parse_args()

    encrypt = args.mode == "enc"
    print(process_message(args.message, args.key, encrypt))
