import sys
import base64

if len(sys.argv) != 3:
    print("Error: Two arguments are required.")
    sys.exit(1)

mode = sys.argv[1]
input_string = sys.argv[2]

if mode == "crypt":
    encrypted_string = base64.b64encode(input_string.encode()).decode()
    print("Encrypted string:", encrypted_string)
elif mode == "decrypt":
    try:
        decrypted_string = base64.b64decode(input_string.encode()).decode()
        print("Decrypted string:", decrypted_string)
    except base64.binascii.Error as e:
        print("Error: Invalid input for decryption.")
        sys.exit(1)
else:
    print("Error: Invalid mode. Please use 'crypt' or 'decrypt'.")
    sys.exit(1)
