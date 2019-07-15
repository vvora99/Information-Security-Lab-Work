from ColumnarEncryption import *

deciphertable=ciphertable[:]
count=0
for col in range(len(ciphertable[0])):
    for row in range(len(ciphertable)):
        deciphertable[row][col]=ciphertext[count]
        count=count+1

plaintable=[]
for i in range(len(key)):
    temp=[]
    ch=keylist[i]
    ind=sortedkeylist.index(ch)
    for row in range(len(ciphertable)):
        for col in range(len(ciphertable[0])):
            if col==ind:
                temp.append(deciphertable[row][col])
    plaintable.append(temp)

plaintable2=[]
for col in range(len(plaintable[0])):
    temp=[]
    for row in range(len(plaintable)):
        temp.append(plaintable[row][col])
    plaintable2.append(temp)

plaintext=''
for arr in plaintable2:
    for ch in arr:
        if ch=="$":
            ch=" "
        if ch=="#":
            ch=''
        plaintext=plaintext+ch
print(plaintext)
