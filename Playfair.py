def prepare(text, key):
    text = "".join(text.split())  # to remove white spaces
    alphabetAndKey = key + list("abcdefghiklmnonpqrstuvwxyz")
    # create a 1d matrix that contains the key and alphabets
    # with no redundant letters
    oneDmatrix = []
    for x in alphabetAndKey:
        if x not in oneDmatrix:
            if x == "i" or x == "j":
                x = "i"
            oneDmatrix.append(x)
    #print(oneDmatrix)

    # transform to two dimensional matrix, with each row 5 elements
    n = 5
    # global twoDmatrix
    twoDmatrix = [oneDmatrix[i:i + 5] for i in range(0, len(oneDmatrix), n)]
    #print(twoDmatrix)

    # separate the plaintext into blocks of size 2:
    n = 2
    # global plain
    plain = []
    i = 0
    while (i < len(text)):
        if i + 1 == len(text):
            plain.append([text[i], 'x'])
            i += 1
        elif text[i] == text[i + 1]:
            plain.append([text[i], 'x'])
            i += 1
        else:
            plain.append(list(text[i:i + n]))
            i += 2
    #print(plain)
    return twoDmatrix, plain


def playfair():
    operation = input("Choose between encrypting or decrypting (e/d): ")
    key = list(input("Enter you key: "))
    result = ""
    if operation == 'e':
        text = input("Enter your PlainText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        # create the matrix and split the plain text into blocks
        twoDmatrix, plain = prepare(text, key) # creates two global variables: twoDmatrix, and plain
        # encipher the text
        for i in range(len(plain)):
            for j in range(len(twoDmatrix)):
                if twoDmatrix[j].count(plain[i][0]) == 1:
                    row1 = j
                    col1 = twoDmatrix[j].index(plain[i][0])
                if twoDmatrix[j].count(plain[i][1]) == 1:
                    row2 = j
                    col2 = twoDmatrix[j].index(plain[i][1])
            if row1 == row2: # shift left
                result += twoDmatrix[row1][(col1+1)%5] + twoDmatrix[row2][(col2+1)%5]
            elif col1 == col2: # shift down
                result += twoDmatrix[(row1+1)%5][col1] + twoDmatrix[(row2+1)%5][col2]
            else:
                result += twoDmatrix[row1][col2] + twoDmatrix[row2][col1]
    elif operation == 'd':
        text = input("Enter your CipherText: ").strip()
        twoDmatrix, plain = prepare(text, key)
        # decipher the text
        for i in range(len(plain)):
            for j in range(len(twoDmatrix)):
                if twoDmatrix[j].count(plain[i][0]) == 1:
                    row1 = j
                    col1 = twoDmatrix[j].index(plain[i][0])
                if twoDmatrix[j].count(plain[i][1]) == 1:
                    row2 = j
                    col2 = twoDmatrix[j].index(plain[i][1])
            if row1 == row2: # shift right
                result += twoDmatrix[row1][col1-1] + twoDmatrix[row2][col2-1]
            elif col1 == col2: # shift up
                result += twoDmatrix[row1-1][col1] + twoDmatrix[row2-1][col2]
            else:
                result += twoDmatrix[row1][col2] + twoDmatrix[row2][col1]
    else:
        print("Invalid input")
    print(result)
playfair()