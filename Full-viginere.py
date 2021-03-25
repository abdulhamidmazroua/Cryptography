# 26 * 26 matrix of alphabets
# each row is shifted left considering the previous row
# It means each row begins with the second letter in the previous row
# the problem is to find the intersection (cipher) between the key (the rows) and the plaintext (the columns)
def prepare():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    global matrix
    matrix = []
    for x in range(len(alphabet)):
        matrix.append(list(alphabet[x:])+list(alphabet[:x]))
    #print(matrix)
def full_vigenere():
    operation = input("Choose between encrypting or decrypting (e/d): ")
    key = str(input("Enter you key : "))
    result = ""
    if operation == 'e':
        text = input("Enter you PlainText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        prepare()
        for x in range(len(text)):
            row = ord(key[x%len(key)]) - 97
            col = ord(text[x]) - 97
            result += matrix[row][col]
    elif operation == 'd':
        text = input("Enter you CipherText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        prepare()
        for x in range(len(text)):
            row = ord(key[x % len(key)]) - 97
            plain = matrix[row].index(text[x]) # find the index of the cipher inside the key row (finding the column that represents the plain text)
            result += chr(plain + 97)
    else:
        print("Invalid input")
    print(result)
full_vigenere()