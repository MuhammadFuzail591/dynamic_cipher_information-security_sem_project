
def calculate_depth(key):
    ascii_sum = sum(ord(c) for c in key.upper())
    depth = (ascii_sum % 5) + 3
    print("\n--- STEP 3: Rail Fence Depth Calculation ---")
    print("ASCII Sum of Key:", ascii_sum)
    print("Calculated Rail Depth:", depth)
    return depth


def rail_fence_encrypt(text, depth):
    print("\n--- STEP 4: Rail Fence Encryption ---")
    print("Input Text:", text)
    print("Rail Depth:", depth)

    rails = ['' for _ in range(depth)]
    rail = 0
    direction = 1

    for ch in text:
        rails[rail] += ch
        rail += direction
        if rail == 0 or rail == depth - 1:
            direction *= -1

    for i, r in enumerate(rails):
        print(f"Rail {i}: {r}")

    output = ''.join(rails)
    print("Output after Rail Fence:", output)
    return output
