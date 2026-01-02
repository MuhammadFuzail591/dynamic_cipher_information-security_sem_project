def build_monoalphabetic_map(key):
    key = key.upper()[::-1]  # reverse key
    seen = set()
    mapping_sequence = []

    # add reversed key characters
    for ch in key:
        if ch not in seen:
            seen.add(ch)
            mapping_sequence.append(ch)

    # add remaining alphabet
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            mapping_sequence.append(ch)

    # build mapping dictionary
    mapping = {}
    for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        mapping[ch] = mapping_sequence[i]

    return mapping


def monoalphabetic_encrypt(text, key):
    mapping = build_monoalphabetic_map(key)
    return ''.join(mapping[ch] for ch in text)
