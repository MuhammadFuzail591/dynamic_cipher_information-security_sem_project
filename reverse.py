def char_to_reverse_num(c):
    # A=25, B=24, ..., Z=0
    return 25 - (ord(c) - ord('A'))

def reverse_num_to_char(n):
    return chr(ord('A') + (25 - n))
