import math
p = int(input("p = "))
q = int(input("q = "))

n = p*q
z = (p-1)*(q-1)

# now we need to find and e that is less than z and relatively prime with z
e=2
while(e < z):
    if(math.gcd(e, z) == 1):
        break
    else:
        e+=1

def modularInverse(x, y): # modular inverse of x mod y
    for d in range(0, y):
        if(x * d % y == 1):
            return d
d = modularInverse(e, z) # d is the modular inverse of e mod z

# choose the operation:
operation = input("Choose between encrypting or decrypting (e/d): ")
# in encryption we use the receiver's public key (e) and n
if (operation == 'e'):
    m = input("Enter your message here: ")
    index = ord(m) - 97 # index of the plain letter
    cipher = index**e % n
    print("public key of the receiver = ", e)
    print("cipher message is: ", cipher)
# in decryption we use the receiver private key (d) and n
elif (operation == 'd'):
    c = int(input("Enter you cipher here: "))
    plain = c**d % n
    print("private key of the receiver = ", d)
    print("plain message is ", plain)
else:
    print("invalide choice")