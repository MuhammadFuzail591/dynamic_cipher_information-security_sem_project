from cipher import encrypt

def run_test(test_id, plaintext, key):
    print("=" * 60)
    print(f"Test Case {test_id}")
    print("Plaintext :", plaintext)
    print("Key       :", key)

    ciphertext, depth = encrypt(plaintext, key)

    print("Calculated Depth :", depth)
    print("Actual Ciphertext:", ciphertext)


    print("=" * 60 + "\n")


def main():
    run_test(
        test_id=1,
        plaintext="HELLO",
        key="UPGRADE"
    )

    run_test(
        test_id=2,
        plaintext="AAAAA",
        key="SECURITY"
    )

    run_test(
        test_id=3,
        plaintext="INFORMATIONSECURITY",
        key="NETWORK"
    )

    run_test(
        test_id=4,
        plaintext="CRYPTOGRAPHY",
        key="KEY"
    )

    run_test(
        test_id=5,
        plaintext="DATA",
        key="AB"
    )


if __name__ == "__main__":
    main()
