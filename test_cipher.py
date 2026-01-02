from cipher import encrypt

def run_test(test_id, plaintext, key, expected_cipher=None):
    print("=" * 60)
    print(f"Test Case {test_id}")
    print("Plaintext :", plaintext)
    print("Key       :", key)

    ciphertext, depth = encrypt(plaintext, key)

    print("Calculated Depth :", depth)
    print("Actual Ciphertext:", ciphertext)

    if expected_cipher:
        print("Expected Cipher  :", expected_cipher)
        if ciphertext == expected_cipher:
            print("STATUS : ✅ PASS")
        else:
            print("STATUS : ❌ FAIL")
    else:
        print("Expected Cipher  : (Not predefined)")
        print("STATUS : ⚠️ MANUAL VERIFICATION")

    print("=" * 60 + "\n")


def main():
    # Test 1: Simple word
    run_test(
        test_id=1,
        plaintext="HELLO",
        key="UPGRADE"
    )

    # Test 2: Repeated characters
    run_test(
        test_id=2,
        plaintext="AAAAA",
        key="SECURITY"
    )

    # Test 3: Longer plaintext
    run_test(
        test_id=3,
        plaintext="INFORMATIONSECURITY",
        key="NETWORK"
    )

    # Test 4: Short key
    run_test(
        test_id=4,
        plaintext="CRYPTOGRAPHY",
        key="KEY"
    )

    # Test 5: Edge case (minimum rail depth handling)
    run_test(
        test_id=5,
        plaintext="DATA",
        key="AB"
    )


if __name__ == "__main__":
    main()
