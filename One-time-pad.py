# key is generated once
# key is equal to the size of the plaintext
# key and plain text are transformed into the binary form
# to encrypt: binary cipher = binary plain xor binary key
# to decrypt: binary plain = binary cipher xor binary key
def onetimepad():
    operation = input("Choose between encrypting or decrypting (e/d): ")
    key = str(input("Enter you key (Note that this is a one time pad key, which means the key must be exactly equal to the plain/cipher text to get a resonable result): "))
    result = ""
    if operation == 'e':
        text = input("Enter your PlainText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        if len(text) != len(key):
            print("Sorry, your key does not equal to the plaintext you have entered")
            return
        for x in range(len(text)):
            asci = ord(text[x]) ^ ord(key[x])
            cipher = str(bin(asci))
            result += cipher[2:]
    elif operation == 'd':
        text = input("Enter your CipherText: ").strip()
        if len(text) != len(key):
            print("Sorry, your key does not equal to the ciphertext you have entered")
            return
        for x in range(len(text)):
            asci = ord(text[x]) ^ ord(key[x])
            plain = str(bin(asci))
            result += plain[2:]
    else:
        print("Invalid input")
    print(result)
onetimepad()
