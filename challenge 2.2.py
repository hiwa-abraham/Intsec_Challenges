import hashlib

# Step 1: Define keys (must be bytes)
key_1 = b"1234"
key_2 = b"5678"

# Step 2: Define messages
messages = {
    "Message 1": b"Challenge 2.2 is easy.",
    "Message 2": b"Challenge 2.2 is doable.",
    "Message 3": b"Challenge 2.2 is hard."
}


for name, msg in messages.items():
    print(name, msg)

# Step 3: Given HMACs (hex strings)
given_hmacs = {
    "Message 1": "12d44a1c2448cc54ddffc75e69313a7964d5d775",
    "Message 2": "1b25d0e281f73935f7a122c088c1bc34686b271b",
    "Message 3": "aec64e480f251c6811686597305b04edcc25da35"
}

# Step 4: Custom HMAC function
def custom_hmac(key1, key2, message):
    # h(key1 || message)
    inner_hex = hashlib.sha1(key1 + message).hexdigest().encode()

    # h(key2 || inner_hash)
    final_hash = hashlib.sha1(key2 + inner_hex).hexdigest()

    return final_hash

# Step 5: Verify each message
for name, msg in messages.items():
    computed_hmac = custom_hmac(key_1, key_2, msg)
    given_hmac = given_hmacs[name]

    print(f"{name}")
    print(f"  Computed HMAC: {computed_hmac}")
    print(f"  Given HMAC:    {given_hmac}")

    if computed_hmac == given_hmac:
        print("  ✅ NOT tampered\n")
    else:
        print("  ❌ TAMPERED\n")