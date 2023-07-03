from Crypto.Cipher import AES
from Crypto import Random
import hashlib

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

plain_text = "I spent a whole day on this god damn script"
print("Plain Text:", plain_text)

key = hashlib.sha256(b'666').digest()
print("Key:", key.hex())

pad_plain_text = pad(plain_text)
iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = (iv + cipher.encrypt(pad_plain_text.encode()))
print("Ciphered text:", cipher_text.hex())

for key_num in range(1, 1000):
    key_num_hash = hashlib.sha256(str(key_num).encode()).digest()
    unpad = lambda s: s[:-ord(s[len(s)-1:])]
    iv = cipher_text[:BS]
    cipher = AES.new(key_num_hash, AES.MODE_CBC, iv)
    try:
        decrypted_text = unpad(cipher.decrypt(cipher_text[BS:])).decode('utf-8', errors='replace')
    except UnicodeDecodeError:
        decrypted_text = "Decoding Error"
    #if key_num_hash == key:
    if decrypted_text == plain_text:
        print("Key found:", key_num)
        print("Key_hash found:", key_num_hash)
        print("Decrypted text:", decrypted_text)
        break
    else:
        print(key_num, "is wrong"
