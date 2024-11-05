

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


def string_to_binary(s):
    return ' '.join(f'{ord(c):08b}' for c in s)


def main() -> None:
    data = input()
    print(string_to_binary(data))
    crc8 = get_crc8(data)
    crc16 = get_crc16(data)
    print(f'CRC8: {crc8:08b}')
    print(f'CRC16: {crc16:08b}')


if __name__ == '__main__':
    main()
