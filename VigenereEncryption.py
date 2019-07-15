import math

charvalue=[]
i=0
for ch in range(97,123,1):
    temp=[]
    temp.append(chr(ch))
    temp.append(i)
    charvalue.append(temp)
    i=i+1

def integer(ch):
    for arr in charvalue:
        if ch==arr[0]:
            return arr[1]

def char(val):
    for arr in charvalue:
        if val==arr[1]:
            return arr[0]

plain=str(input("Enter Plain Text"))
plain=plain.lower()
list1=plain.split()
plain=''
for val in list1:
    plain=plain+val

key=str(input("Enter Key"))
lplain=len(plain)
lkey=len(key)
r=math.ceil(lplain/lkey)

nkey=''
for i in range(r):
    nkey=nkey+key
    nkey=nkey.lower()

newkey=''
if len(nkey)!=len(plain):
    d=len(nkey)-len(plain)
    newkey=nkey[0:len(nkey)-d]
else:
    newkey=nkey

ciphertext=''
for i in range(len(plain)):
    ch=plain[i]
    k=newkey[i]
    nch=integer(ch)
    nk=integer(k)
    ntotal=nch+nk
    ch=char(ntotal%26)
    ciphertext=ciphertext+ch

print("plain : ",plain)
print("key : ",key)
print("Ciphertext : ",ciphertext)
