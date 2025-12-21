import hashlib

target = "d249bf47a16435ed04f3c2d52ea29459"
salt = "c036"

# Try to load rockyou.txt
try:
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
        passwords = [line.strip() for line in f]
    print("Using rockyou.txt wordlist.")
except FileNotFoundError:
    # Fallback: extended manual list
    passwords = [
        "under", "nose", "your", "password", "123456", "admin", "letmein",
        "c036", "salt", "hash", "md5", "d249", "bf47", "1643", "5ed0",
        "4f3c", "2d52", "ea29", "459", "under_your_nose", "under your nose",
        "Under", "Nose", "Your", "underdog", "sunshine", "monkey", "dragon",
        "football", "baseball", "mustang", "michael", "shadow", "master",
        "jennifer", "111111", "qwerty", "password123", "admin123", "welcome",
        "abc123", "letmein123", "123123", "654321", "superman", "1qaz2wsx",
        "qazwsx", "password1", "12345678", "123456789", "1234567890",
        "000000", "pass", "pass123", "secret", "test", "testing", "hello",
        "world", "computer", "internet", "hacker", "hack", "security"
    ]
    print("Using fallback wordlist.")

# Try each password
for pwd in passwords:
    test = pwd + salt
    h = hashlib.md5(test.encode()).hexdigest()
    if h == target:
        print(f"\nPassword found: {pwd}")
        print(f"String hashed: {test}")
        print(f"Hash matches: {h}")
        break
else:
    print("\nPassword not found in wordlist.")