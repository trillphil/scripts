#!/usr/bin/env python3

def type7_decrypt(enc_pwd):
    xlat = [0x64, 0x73, 0x66, 0x64, 0x3b, 0x6b, 0x66, 0x6f, 0x41, 0x2c, 0x2e, 0x69, 0x79,
        0x65, 0x77, 0x72, 0x6b, 0x6c,  0x64, 0x4a, 0x4b, 0x44, 0x48, 0x53, 0x55, 0x42]
    index = int(enc_pwd[:2])
    enc_pwd = enc_pwd[2:].rstrip()
    pwd_hex = [enc_pwd[x:x + 2] for x in range(0, len(enc_pwd), 2)]
    cleartext = [chr(xlat[index+i] ^ int(pwd_hex[i], 16)) for i in range(0, len(pwd_hex))]

    print("[*] Result: %s" % ''.join(cleartext))


def main():

    type7_decrypt('143346253B033F2E2C26093B')


if __name__ == '__main__':
    main()


