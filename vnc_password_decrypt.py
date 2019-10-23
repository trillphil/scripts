#!/usr/bin/env python3
import argparse
from des import DesKey


def decrypt_ultravnc(password):
    key = bytes.fromhex('E84AD660C4721AE0')
    des = DesKey(key)
    input_password = password

    if len(input_password) == 16:
        clear=des.decrypt(bytes.fromhex(input_password))
        return clear.decode('utf-8')
    

def main():

    parser = argparse.ArgumentParser(description='VNC Password Decryptor',
                        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--type',
                        '-t',
                        help="VNC server type",
                        default="ultravnc")
    parser.add_argument('password', help="the encrypted password")
    args = parser.parse_args()
    
    if args.type == "ultravnc":
        clear = decrypt_ultravnc(args.password)
    else:
        print(f"[!] Password decryption for '{args.type}' not implemented")
        clear = None

    if clear != None:
        print(f"[*] Decrypted Password: {clear}")

if __name__ == '__main__':
    main()
