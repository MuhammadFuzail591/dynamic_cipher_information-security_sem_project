from reverse import char_to_reverse_num, reverse_num_to_char

def dynamic_caesar_encrypt(plaintext, key):
    print("\n--- STEP 1: Dynamic Caesar Cipher ---")
    print("Input Plaintext:", plaintext)
    print("Key:", key)

    plaintext = plaintext.upper()
    key = key.upper()
    key_len = len(key)

    result = []

    for i, ch in enumerate(plaintext):
        p_val = char_to_reverse_num(ch)
        k_val = char_to_reverse_num(key[i % key_len])
        shift = (k_val + i) % 26
        c_val = (p_val + shift) % 26
        c_char = reverse_num_to_char(c_val)

        print(f"Char '{ch}' | P={p_val}, K={k_val}, i={i}, Shift={shift} → {c_char}")

        result.append(c_char)

    output = ''.join(result)
    print("Output after Caesar:", output)
    return output
