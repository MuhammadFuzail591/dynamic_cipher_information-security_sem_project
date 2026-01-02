
def calculate_depth(key):
    ascii_sum = sum(ord(c) for c in key)
    depth = ascii_sum % len(key)
    return depth if depth >= 2 else 2


def rail_fence_encrypt(text, depth):
    rails = ['' for _ in range(depth)]
    rail = 0
    direction = 1  # 1 = down, -1 = up

    for ch in text:
        rails[rail] += ch
        rail += direction

        if rail == 0 or rail == depth - 1:
            direction *= -1

    return ''.join(rails)
