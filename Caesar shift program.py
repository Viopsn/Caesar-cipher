shift = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
shift2 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
enORde = input("Would you like to encrypt or decrypt a message (E/D)? ").lower()
numMessage = []
numEncrypted = []
numKey = []
encrypted = []
message = []
count = 0

if enORde == 'e':
    key = input("""
Enter the KEY the message should be encrypted with.
This can be a number (26 or less), a letter or a word (no spaces).
\t""")
    message = input("Enter the MESSAGE you want to encrypt:\n\t").lower()

    #convert the message into numbers
    for word in message:
        for letter in word:
            try:
                number = shift[letter]
                numMessage.append(number)
            except:
                numMessage.append(letter)
                
    #convert the key into numbers           
    try:
        numKey.append(int(key))
    except:
        for letter in key:
            number = shift[letter]
            numKey.append(number)
        
    #add the key to each number of the message, and take 26 if the number is >26
    #       (to get the shift to wrap back round to 'a'), to get each number of
    #       the encrypted message
    for x in numMessage:
        try:
            x = x+numKey[count]
            while x>26:
                x=x-26
            numEncrypted.append(x)
            count += 1
        except:
            numEncrypted.append(x)
        if count>=len(numKey):
            count = 0

    #convert the numbers of the encrypted message to the letters
    for x in numEncrypted:
        try:
            letter = shift2[x]
            encrypted.append(letter)
        except:
            encrypted.append(x)
    
    print("\nYour encrypted message:")
    print(*encrypted)

elif enORde == 'd':
    key = input("""
Enter the KEY the message was encrypted with.
This can be a number (26 or less), a letter or a word (no spaces).
\t""")
    encrypted = input("Enter the MESSAGE you want to decrypt:\n\t")

    #convert the letters of the encrypted message into numbers
    for word in encrypted:
        for letter in word:
            try:
                number = shift[letter]
                numEncrypted.append(number)
            except:
                numEncrypted.append(letter)

    #convert the key into numbers           
    try:
        numKey.append(int(key))
    except:
        for letter in key:
            number = shift[letter]
            numKey.append(number)

    #minus the key from each number of the encrypted message, and add 26 if the
    #       number is <1(to get the shift to wrap back round to 'z'), to get each
    #       number of the message
    for x in numEncrypted:
        try:
            x = x-numKey[count]
            while x<1:
                x=x+26
            numMessage.append(x)
            count += 1
        except:
            numMessage.append(x)
        if count>=len(numKey):
            count = 0

    #convert the numbers of the message to the letters
    for x in numMessage:
        try:
            letter = shift2[x]
            message.append(letter)
        except:
            message.append(x)

    print("\nYour decrypted message:")
    print(*message)


else:
    print("That input was invalid.")
