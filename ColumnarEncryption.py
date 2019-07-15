import math
plain=str(input("Enter Plain text : "))
key=str(input("Enter Key : "))

table=[]
cols=len(key)
rows=math.ceil(len(plain)/len(key))
count=0
for r in range(rows):
    temp=[]
    for c in range(cols):
        if count>len(plain)-1:
            temp.append("#")
        else:
            ch=plain[count].lower()
            if ch==" ":
                temp.append("$")
            else:
                temp.append(ch)
        count=count+1
    table.append(temp)
print(table)

keylist=[]
for i in key:
    keylist.append(i)

keylist1=keylist[:]

sortedkeylist=[]
for i in range(len(key)):
    minkey=min(keylist1)
    minkeyind=keylist1.index(minkey)
    sortedkeylist.append(minkey)
    keylist1[minkeyind]='z'

ciphertable=[]
for ch in sortedkeylist:
    temp=[]
    sortedind=keylist.index(ch)
    for row in range(len(table)):
        for col in range(len(table[0])):
            if col==sortedind:
                temp.append(table[row][col])
    ciphertable.append(temp)
print(ciphertable)

ciphertext=''
for arr in ciphertable:
    for ch in arr:
        ciphertext=ciphertext+ch
print(ciphertext)
