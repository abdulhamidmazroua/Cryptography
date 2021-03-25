def caesar():
    operation = input("Choose between encrypting or decrypting (e/d): ")
    key = int(input("Enter you key: "))
    result = ""
    if operation == "e":
        text = input("Enter your PlainText: ").strip()
        text = "".join(text.split()) # to remove white spaces
        for x in range(len(text)):
            index = ord(text[x]) - 97
            index = (index + key) % 26
            result += chr(index + 97)
    elif operation == "d":
        text = input("Enter you CipherText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        for x in range(len(text)):
            index = ord(text[x]) - 97
            index = (index - key) % 26
            result += chr(index + 97)
    else:
        print("Invalid input")
    print(result)
caesar()