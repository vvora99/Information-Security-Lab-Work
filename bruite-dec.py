f1=open("enc.txt")
f2=open("dec.txt")
val1=f1.read()
val2=f2.read()

print("Actual Data:")
print(val1)
print("Encrypted Data:")
print(val2)

print("Find The Key Usinf Bruite Force:")

l1=[]
l2=[]
for i in val1:
	l1.append(i)
for i in val2:
	l2.append(i)

ltemp=[]

for k in range(0,256,1):
	for i in val2:
		ltemp.append(chr((ord(i)-k)%255))
	if(ltemp==l1):
		print('key is : ')
		print(k)
		print(val1)
		break
	ltemp=[]
