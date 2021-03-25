# it is also called simple left shift vigener cipher
def polyalphabetic():
    operation = input("Choose between encrypting or decrypting (e/d): ")
    key = str(input("Enter you key: "))
    result = ""
    if operation == "e":
        text = input("Enter your PlainText: ").strip()
        text = "".join(text.split()) # to remove white spaces
        for x in range(len(text)):
            index = ord(text[x]) - 97   # to get the plain letter index
            currentKey = ord(key[x%len(key)]) - 97   # to get the current key
            index = (index + currentKey) % 26 # to get the cipher index
            result += chr(index + 97)
    elif operation == "d":
        text = input("Enter you CipherText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        for x in range(len(text)):
            index = ord(text[x]) - 97   # to get the cipher letter index
            currentKey = ord(key[x % len(key)]) - 97  # to get the current key
            index = (index - currentKey) % 26  # to get the plain index
            result += chr(index + 97)
    else:
        print("Invalid input")
    print(result)
polyalphabetic()