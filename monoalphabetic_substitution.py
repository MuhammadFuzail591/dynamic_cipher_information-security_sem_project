def build_monoalphabetic_map(key):
    key = key.upper()[::-1]
    seen = set()
    seq = []

    for ch in key:
        if ch not in seen:
            seen.add(ch)
            seq.append(ch)

    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seq.append(ch)

    return dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", seq))


def monoalphabetic_encrypt(text, key):
    print("\n--- STEP 2: Monoalphabetic Substitution ---")
    print("Input Text:", text)

    mapping = build_monoalphabetic_map(key)
    print("Substitution Mapping:")
    for k, v in mapping.items():
        print(f"{k} → {v}", end=" | ")
    print("\n")

    result = ''.join(mapping[ch] for ch in text)
    print("Output after Substitution:", result)
    return result
