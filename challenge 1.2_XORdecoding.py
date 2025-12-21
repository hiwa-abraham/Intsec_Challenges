# challenge1.2 — FIXED
input_file = r"H:\infosec-project\Challenges\challenge1.2.enc"
output_file = "challenge1.2_decrypted.txt"

with open(input_file, "rb") as f:
    encrypted = f.read()

# ✅ CORRECT KEY: 15 bytes — "ashortpassword" + newline (\n = 0x0A)
key = b"ashortpassword\n"  # len = 15
print(f"🔑 Using key: {key} (length: {len(key)} bytes)")

# Decrypt with repeating XOR
decrypted = bytearray()
for i in range(len(encrypted)):
    decrypted.append(encrypted[i] ^ key[i % len(key)])

# Decode safely (some bytes may be non-ASCII in padding — ignore errors)
try:
    text = decrypted.decode('utf-8')
except UnicodeDecodeError:
    text = decrypted.decode('ascii', errors='replace')

print("\n" + "="*70)
print("✅ DECRYPTED OUTPUT (Challenge 1.2)")
print("="*70)
print(text)
print("="*70)

# Save cleaned result (strip trailing nulls/garbage if any)
clean_text = text.rstrip('\x00\r\n ') + '\n'
with open(output_file, "w", encoding="utf-8") as f:
    f.write(clean_text)

print(f"\n💾 Saved clean output to: {output_file}")