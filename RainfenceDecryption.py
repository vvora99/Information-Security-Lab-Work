from RailfenceEncryption import *

l=len(ciphertext)
rows=depth
cols=l

newmatrix=[]
for i in range(rows):
    temp=[]
    for j in range(cols):
        temp.append(" ")
    newmatrix.append(temp)

c=0
for r in rowindexlist:
    if c<=cols-1:
        newmatrix[r][c]="*"
        c=c+1

count=0
for i in range(rows):
    for j in range(cols):
        if newmatrix[i][j]=="*":
            newmatrix[i][j]=ciphertext[count]
            count=count+1
print(newmatrix)

decrypted=''
for c in range(cols):
    for r in range(rows):
        if newmatrix[r][c]!=" ":
            decrypted=decrypted+newmatrix[r][c]
print("Decrypted : ",decrypted)
