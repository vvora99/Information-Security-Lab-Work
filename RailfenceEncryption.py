import math

plain=str(input("Enter plain text : "))
depth=int(input("Enter depth"))

l=len(plain)

rows=depth
cols=l

matrix=[]
for r in range(rows):
    temp=[]
    for c in range(cols):
        temp.append(' ')
    matrix.append(temp)

rowindexlist=[]
for count in range(0,l,((2*rows)-2)):
    for i in range(0,rows,1):
        rowindexlist.append(i)
    for i in range(rows-2,0,-1):
        rowindexlist.append(i)

c=0
for i in range(len(plain)):
    ch=plain[i]
    r=rowindexlist[i]
    matrix[r][c]=ch
    c=c+1

ciphertext=''
for list1 in matrix:
    for ch in list1:
        if ch!=' ':
            ciphertext=ciphertext+ch
print("Ciphertext : ",ciphertext)
