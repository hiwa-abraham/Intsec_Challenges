#!/usr/bin/env python3
"""
INTSEC VT 2025 – Challenge 3.4
Optimized and correct solution
"""

import hashlib


# =========================
# TinyH (correct definition)
# =========================

def tinyh(x: int) -> int:
    hex_str = f"{x:04x}"          # hash hex string, not raw bytes
    return int.from_bytes(
        hashlib.sha1(hex_str.encode()).digest()[:2],
        "big"
    )


# =========================
# Bob attack (OPTIMIZED)
# =========================

def attack_bob():
    print("=== Bob Attack ===")

    otp_a = int("f25a", 16)
    otp_b = int("cbc9", 16)

    MAX_N = 200

    for mp in range(0x0000, 0x10000):

        # Precompute TinyH chain
        chain = [mp]
        for _ in range(MAX_N + 2):
            chain.append(tinyh(chain[-1]))

        for n in range(1, MAX_N):
            otp_n = chain[n] ^ mp
            otp_n1 = chain[n + 1] ^ mp

            if otp_n == otp_a and otp_n1 == otp_b:
                next_otp = chain[n + 2] ^ mp

                print(f"Recovered master password: {mp:04x}")
                print(f"Counter at first observed OTP: {n}")
                print(f"Bob's next OTP: {next_otp:04x}")
                print()
                return

    print("Master password not found!")


# =========================
# Main
# =========================

def main():
    attack_bob()


if __name__ == "__main__":
    main()
