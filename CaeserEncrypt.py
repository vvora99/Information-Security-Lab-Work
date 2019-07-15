'''key=3
f=open("enc.txt")
f1=open("dec.txt",'w')
ch=f.read(1)
while(ch):
	val=ord(ch)
	enckey=(val+key)%255
	encval=chr(enckey)
	f1.write(encval)
	ch=f.read(1)
f.close()
'''

plain=str(input("Enter plain text : "))
key=int(input("Enter key (int only) : "))
ciphertext=''
for ch in plain:
        val=ord(ch)
        enckey=(val+key)%255
        encval=chr(enckey)
        ciphertext=ciphertext+encval
print("Encrypted : ",ciphertext)
