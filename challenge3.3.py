import argon2
import time
import secrets

# Create an Argon2 hasher instance with Argon2id
hasher = argon2.PasswordHasher(
    type=argon2.Type.ID,  # Argon2id variant
    memory_cost=65536,     # 64 MB
    time_cost=3,           # 3 iterations
    parallelism=4,         # 4 parallel threads
    hash_len=32,           # 32 bytes hash length
    salt_len=16            # 16 bytes salt length
)

# Generate and hash 10000 random values
hashes = []
start_time = time.time()

for i in range(10000):
    # Generate a random value to hash
    random_value = secrets.token_hex(32)
    
    # Compute the hash
    hash_result = hasher.hash(random_value)
    hashes.append(hash_result)
    
    # Print progress every 1000 hashes
    if (i + 1) % 1000 == 0:
        print(f"Completed {i + 1} hashes...")

end_time = time.time()
print(f"\nCompleted 10,000 Argon2id hashes in {end_time - start_time:.2f} seconds")
print(f"Average time per hash: {(end_time - start_time) / 10000:.4f} seconds")

# Show a few example hashes
print("\nFirst 3 example hashes:")
for i in range(3):
    print(f"Hash {i+1}: {hashes[i][:50]}...")  # Show first 50 chars