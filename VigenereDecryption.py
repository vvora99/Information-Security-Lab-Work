from VigenereEncryption import *

newplain=''
for i in range(len(ciphertext)):
    ch=ciphertext[i]
    k=newkey[i]
    nch=integer(ch)
    nk=integer(k)
    ntotal=nch-nk
    ch=char(ntotal%26)
    newplain=newplain+ch

print("Decrypted : ",newplain)
    
