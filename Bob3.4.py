import hashlib

def TinyH(a):
    """TinyH(a) = first 16 bits of SHA1(a)"""
    a_hex = a.zfill(4)
    digest = hashlib.sha1(a_hex.encode("ascii")).digest()
    msb16 = int.from_bytes(digest[:2], byteorder="big")
    return f"{msb16:04x}"

def find_mp():
    for mp_int in range(0x10000):  # 0 to 65535
        mp = f"{mp_int:04x}"
        
        # First OTP: n=1
        H1 = TinyH(mp)
        otp1 = f"{int(H1, 16) ^ int(mp, 16):04x}"
        
        if otp1 == "f25a":
            # Second OTP: n=2
            H2 = TinyH(H1)
            otp2 = f"{int(H2, 16) ^ int(mp, 16):04x}"
            
            if otp2 == "cbc9":
                # Check next OTP: n=3 (what Alice would use)
                H3 = TinyH(H2)
                otp3 = f"{int(H3, 16) ^ int(mp, 16):04x}"
                return mp, otp3
    return None

result = find_mp()
print(f"Found mp: {result[0]}, Next OTP: {result[1]}")