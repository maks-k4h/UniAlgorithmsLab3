## Lab3 Report

**No.9 -> variant 1**

We implement simple CRC for 8- and 16-bit control sums.

def get_crc8(data: str):
    G = 0x1D
    crc = 0

    for byte in [ord(c) for c in data]:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = G ^ (crc << 1)
            else:
                crc <<= 1
        crc &= 0xFF

    return crc


def get_crc16(data: str) -> int:
    G = 0xA001
    crc = 0

    for byte in [ord(c) for c in data]:
        crc ^= byte
        for _ in range(8):
            if crc & 0x8000:
                crc = G ^ (crc << 1)
            else:
                crc <<= 1
        crc &= 0xFFFF

    return crc