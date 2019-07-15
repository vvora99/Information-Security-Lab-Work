string=str(input("Enter plain text : "))
stl=string.split()
plain=''
for i in stl:
    plain=plain+i.lower()

matrix=[]
for i in range(6):
    temp=[]
    for j in range(6):
        temp.append(0)
    matrix.append(temp)

key=str(input("Enter key : "))
key=key.lower()

abcd=''
for i in range(97,123,1):
    abcd=abcd+chr(i)
for i in range(0,10,1):
    abcd=abcd+str(i)

string=key+abcd

tempmat=[]
for i in string:
    if i not in tempmat:
        tempmat.append(i)

for i in range(6):
    for j in range(6):
        matrix[i][j]=tempmat[(6*i)+j]

l=len(plain)

plainlist=[]
for i in range(len(plain)):
    temp=[]
    if i%2==0:
        ch1=plain[i]
        if i==l-1:
            ch2='x'
        else:
            ch2=plain[i+1]
        if ch1==ch2:
            ch2='x'
        temp.append(ch1)
        temp.append(ch2)
        plainlist.append(temp)
#print(plainlist)

indexlist=[]
for list1 in plainlist:
    temp=[]
    i1=[]
    i2=[]
    ch1=list1[0]
    ch2=list1[1]
    for xlist in matrix:
        for yele in xlist:
            if yele==ch1:
                x=matrix.index(xlist)
                y=xlist.index(ch1)
                i1.append(x)
                i1.append(y)
                temp.append(i1)
    for xlist in matrix:
        for yele in xlist:
            if yele==ch2:
                x=matrix.index(xlist)
                y=xlist.index(ch2)
                i2.append(x)
                i2.append(y)
                temp.append(i2)
    indexlist.append(temp)
#print(indexlist)

enclist=[]
for list1 in indexlist:
    temp=[]
    nch1=''
    nch2=''
    if list1[0][0]==list1[1][0]:
        if list1[0][1]<=4:
            nch1=matrix[list1[0][0]][list1[0][1]+1]
        else:
            nch1=matrix[list1[0][0]][0]
        if list1[1][1]<=4:
            nch2=matrix[list1[1][0]][list1[1][1]+1]
        else:
            nch2=matrix[list1[1][0]][0]
        temp.append(nch1)
        temp.append(nch2)
    elif list1[0][1]==list1[1][1]:
        if list1[0][0]<=4:
            nch1=matrix[list1[0][0]+1][list1[0][1]]
        else:
            nch1=matrix[0][list1[0][1]]
        if list1[1][0]<=4:
            nch2=matrix[list1[1][0]+1][list1[1][1]]
        else:
            nch2=matrix[0][list1[1][1]]
        temp.append(nch1)
        temp.append(nch2)
    else:
        nch1=matrix[list1[0][0]][list1[1][1]]
        nch2=matrix[list1[1][0]][list1[0][1]]
        temp.append(nch1)
        temp.append(nch2)
    enclist.append(temp)
#print(enclist)

encryptedtext=''
for list1 in enclist:
    for ch in list1:
        encryptedtext=encryptedtext+ch
print("Encrypted text is :")
print(encryptedtext)
