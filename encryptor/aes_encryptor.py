from pbkdf2 import PBKDF2
from Crypto.Cipher import AES
import base64


def pad(s):
    return s + ((16 - len(s) % 16) * '{')


def encrypt(plaintext, password):
    salt = b'\xa0I\x15\xa2\x00W(\xa9'
    
    pad_it = lambda s: bytes(s+(16 - len(s)%16)*'{', encoding='utf-8')
    
    key = PBKDF2(password, salt).read(16)
    generator = AES.new(key, AES.MODE_ECB)
    crypt = generator.encrypt(pad_it(plaintext))
    msg = base64.b64encode(crypt)
    return msg.decode()


def decrypt(ciphertext, password):
    salt = b'\xa0I\x15\xa2\x00W(\xa9'

    key = PBKDF2(password, salt).read(16)
    generator = AES.new(key, AES.MODE_ECB)
    dec = generator.decrypt(base64.b64decode(ciphertext))
    dec = dec.decode()
    padding = dec.count('{')
    return dec[:len(dec)-padding]