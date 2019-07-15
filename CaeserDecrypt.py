'''key=3
f=open("dec.txt",'r')
ch=f.read(1)
while(ch):
	decval=ord(ch)
	val=(decval-key)%255
	encval=chr(val)
	print(encval)
	ch=f.read(1)'''

from CaeserEncrypt import *

decrypted=''
for ch in ciphertext:
    decval=ord(ch)
    val=(decval-key)%255
    encval=chr(val)
    decrypted=decrypted+encval
print("Decrypted: ",decrypted)
