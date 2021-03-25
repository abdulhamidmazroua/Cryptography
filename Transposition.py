# transposition encryption algorithm
# the key is used to form a row
# each column in that row is represented by a number
# the number represents the alphabetic order of that letter relative to the rest of the letters in the key
# then, the plaintext is used to fill the whole matrix
# finally, each column is taken as an input to the cipher text
# columns are taken by the order of the numbers defined earlier
import math
def transposition():
    operation = input("Choose between encrypting or decrypting (e/d): ")
    key = list(input(
        "Enter you key: "))
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if operation == 'e':
        text = input("Enter you PlainText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        plainMatrix = [list(text[x:len(key)+x]) for x in range(0, len(text), len(key)) ]
        i = 0
        while len(plainMatrix[len(plainMatrix) - 1]) != len(key):
            plainMatrix[len(plainMatrix) - 1].append(alphabet[i])
            i += 1
        keyOrder = sorted(key)
        for i in range(len(key)):
            for j in range(len(plainMatrix)):
                result += plainMatrix[j][key.index(keyOrder[i])]

    elif operation == 'd':
        text = input("Enter you CipherText: ").strip()
        text = "".join(text.split())  # to remove white spaces
        colSize = math.ceil(len(text) / len(key))
        # we need to take the first letter of each column
        # but the order in which those columns is presented is critical for the sake of finding the right order for the plaintext

        cipherMatrix = [list(text[i:colSize+i]) for i in range(0, len(text), colSize)] # we first divide the cipher into blocks each block represents a column
        keyOrder = sorted(key)
        ansMatrix = [cipherMatrix[keyOrder.index(key[i])] for i in range(len(cipherMatrix))] # then we rearrange the blocks so that the first block is the column below the first letter in the key
        for x in range(colSize):    # finally, we take every first letter from each block, then every second letter from each block, and so on.
            for y in range(len(ansMatrix)):
                result += ansMatrix[y][x]
    else:
        print("Invalid input")
    print(result)
transposition()