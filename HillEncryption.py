import math
'''key="HILL"
msg="SHORT MESSAGE"'''

msg=str(input("Enter Plain Text "))
key=str(input("Enter Key (either 4 or 9 chars)"))

lkey=math.ceil(math.sqrt(len(key)))

c=0
alphamat=[]
for i in range(97,123,1):
    temp=[]
    temp.append(chr(i))
    temp.append(c)
    c=c+1
    alphamat.append(temp)
#print(alphamat)

c=0
keymat=[]
for i in range(lkey):
    temp=[]
    for j in range(lkey):
        if c>(len(key)-1):
            temp.append('0')
        else:
            temp.append(key[c].lower())
            c=c+1
    keymat.append(temp)
#print(keymat)

keyindexmat=[]
for list1 in keymat:
    temp=[]
    for ch in list1:
        if ch=='0':
            temp.append('0')
        for entry in alphamat:
            if ch==entry[0]:
                temp.append(entry[1])
    keyindexmat.append(temp)
#print(keyindexmat)

plaintext=''
for ch in msg:
    if ch!=' ':
        plaintext=plaintext+ch

noofmat=math.ceil(len(plaintext)/lkey)

counter=0
P=[]
for n in range(0,noofmat,1):
    pi=[]
    for r in range(0,lkey,1):
        for c in range(1,2,1):
            te=[]
            if counter<=len(plaintext)-1:
                ch=plaintext[counter].lower()
                for entry in alphamat:
                    if ch==entry[0]:
                        temp=entry[1]
                        te.append(temp)
                        counter=counter+1
            else:
                te.append('0')
            pi.append(te)
    if len(pi)==lkey:
        P.append(pi)
#print(P)

C=[]
for n in range(0,noofmat,1):
    ci=[]
    for r in range(0,lkey,1):
        temp=[]
        for c in range(0,1,1):
            temp.append(0)
        ci.append(temp)
    pi=P[n]
    ki=keyindexmat
    for i in range(len(keyindexmat)):
        for j in range(len(pi[0])):
            for k in range(len(pi)):
                ci[i][j]=ci[i][j]+(int(keyindexmat[i][k])*int(pi[k][j]))
                ci[i][j]=ci[i][j]%26
    C.append(ci)
#print(C)

ciphertext=''
for list1 in C:
    for list2 in list1:
        for ch in list2:
            for entry in alphamat:
                if ch==entry[1]:
                    t=entry[0]
                    ciphertext=ciphertext+t
print("Plain Text : ",msg)
print("Key : ",key)
print("Ciphertext : ",ciphertext)
