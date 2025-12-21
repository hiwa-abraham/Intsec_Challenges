def caesar_custom_charset(ciphertext, shift, charset):
    """
    Caesar decode ciphertext using custom charset.
    shift: decoding shift (positive = forward in alphabet for encoding, so decode = -shift)
    charset: string of characters in order, positions 0..len(charset)-1
    """
    n = len(charset)
    char_to_index = {ch: i for i, ch in enumerate(charset)}
    
    result = []
    for ch in ciphertext:
        if ch in char_to_index:
            new_index = (char_to_index[ch] - shift) % n
            result.append(charset[new_index])
        else:
            # keep character unchanged if not in charset (shouldn't happen here)
            result.append(ch)
    return ''.join(result)

# Define your charset
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"  # 37 characters

ciphertext = (
    "D_AZ_5H7S006_9WHF6BHD_33HX_5"
    "VHSAH3WS0AHIJHX3SY0H064WH6XH"
    "AZW4HS9WHX_3WH5S4WVHX3SYH5HT"
    "BAH064WA_4W0HAZWHX3SYH_0HZ_V"
    "VW5H_5HS56AZW9HX_3WHAZ_0H4W0"
    "0SYWH_0HAZWHS50DW9HA6HUZS33W"
    "5YWHIHV6AHI"
)

# Remove any spaces/newlines from ciphertext if needed
ciphertext = ciphertext.replace("\n", "").replace(" ", "")

# Try shifts 0 to 36
for shift in range(len(charset)):
    decoded = caesar_custom_charset(ciphertext, shift, charset)
    print(f"Shift {shift:2d}: {decoded[:]}")  # first 50 chars
    # Uncomment next line to see full output for each shift
    # print(f"Shift {shift:2d}: {decoded}")