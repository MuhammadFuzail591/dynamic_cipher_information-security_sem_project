from reverse import char_to_reverse_num
from reverse import reverse_num_to_char

def dynamic_caesar_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    key_len = len(key)

    result = []

    for i, ch in enumerate(plaintext):
        p_val = char_to_reverse_num(ch)
        k_val = char_to_reverse_num(key[i % key_len])

        shift = (k_val + i) % 26
        c_val = (p_val + shift) % 26

        result.append(reverse_num_to_char(c_val))

    return ''.join(result)
