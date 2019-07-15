def invmod(e,fin):
    t1=0
    t2=1
    r1=fin
    r2=e
    while(r2!=0):
        q=r1//r2
        r=r1%r2
        t=t1-(q*t2)
        r1=r2
        r2=r
        t1=t2
        t2=t
    return t1

list1=[]
c=97
for i in range(26):
    temp=[]
    temp.append(chr(c))
    temp.append(i)
    list1.append(temp)
    c=c+1

def char(val):
    for arr in list1:
        if arr[1]==val:
            return arr[0]

def integer(ch):
    for arr in list1:
        if arr[0]==ch:
            return arr[1]

p=167
q=271

n=p*q
fin=(p-1)*(q-1)

print("p : ",p)
print("q : ",q)
print("n : ",n)
print("fi(n) : ",fin)

pose=[]
for i in [3,5,7,11,13,17,19,23,29,31]:
    if fin%i!=0:
        pose.append(i)
print("Possible public key (e) (preferred is 7) : ",pose)
e=int(input("Choose public key (e) from above list : "))

tempd=invmod(e,fin)
if tempd<0:
    d=fin-tempd
else:
    d=tempd
print("private key (d) : ",d)

plain=str(input("Enter plain text : "))
blocksize=3
blockedtext=[]
while len(plain)!=0:
    if len(plain)>blocksize:
        blockedtext.append(plain[:blocksize])
        plain=plain[blocksize:]
    else:
        blockedtext.append(plain)
        plain=plain[len(plain):]
print("blocked text ",blockedtext)

intp=[]
for string in blockedtext:
    i=len(string)-1
    sum1=0
    for ch in string:
        sum1=sum1+(integer(ch)*pow(26,i))
        i=i-1
    intp.append(sum1)
print("Plain text as integers (p) : ",intp)

intc=[]
for p in intp:
    c=pow(p,e)%n
    intc.append(c)
print("Cipher text as integer (c) : ",intc)

cipherstring=''
for c in intc:
    string=''
    while c>0:
        string+=char(c%26)
        c=c//26
    cipherstring=cipherstring+string
cipherstring=cipherstring[::-1]
print("Cipher text : ",cipherstring)

intdec=[]
for c in intc:
    p=pow(c,d)%n
    intdec.append(p)
print("Decrypted text as integer : ",intdec)

decrypted=[]
for c in intdec:
    string=''
    while c>0:
        string+=char(c%26)
        c=c//26
    decrypted.append(string)

decryptedtext=''
for string in decrypted:
    decryptedtext+=string[::-1]
print("Decrypted Text : ",decryptedtext)
