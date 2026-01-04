from dynamic_caeser_cipher import dynamic_caesar_encrypt
from monoalphabetic_substitution import monoalphabetic_encrypt
from rail_fence_dynamic_depth import rail_fence_encrypt
from rail_fence_dynamic_depth import calculate_depth

def encrypt(plaintext, key):
    print("\n================ ENCRYPTION START ================")

    step1 = dynamic_caesar_encrypt(plaintext, key)
    step2 = monoalphabetic_encrypt(step1, key)
    depth = calculate_depth(key)
    ciphertext = rail_fence_encrypt(step2, depth)

    print("\n================ ENCRYPTION END ==================")
    print("FINAL CIPHERTEXT:", ciphertext)

    return ciphertext, depth


encrypt("Hello", key="UPGRADE")