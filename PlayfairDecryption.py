from PlayfairEncryption import *

import math

enclist2=[]
l=len(encryptedtext)
c=math.ceil(l/2)
for i in range(c):
    temp=[]
    for j in range(2):
        if (2*i+j)<=l:
            temp.append(encryptedtext[2*i+j])
        else:
            temp.append(0)
    enclist2.append(temp)

indexlist=[]
for list1 in enclist2:
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
    for xlist in matrix:
        for yele in xlist:
            if yele==ch2:
                x=matrix.index(xlist)
                y=xlist.index(ch2)
                i2.append(x)
                i2.append(y)
    temp.append(i1)
    temp.append(i2)
    indexlist.append(temp)

declist=[]
for list1 in indexlist:
    temp=[]
    nch1=''
    nch2=''
    if list1[0][0]==list1[1][0]:
        if list1[0][1]>=1:
            nch1=matrix[list1[0][0]][list1[0][1]-1]
        else:
            nch1=matrix[list1[0][0]][5]
        if list1[1][1]>=1:
            nch2=matrix[list1[1][0]][list1[1][1]-1]
        else:
            nch2=matrix[list1[1][0]][5]
    elif list1[0][1]==list1[1][1]:
        if list1[0][0]>=1:
            nch1=matrix[list1[0][0]-1][list1[0][1]]
        else:
            nch1=matrix[5][list1[0][1]]
        if list1[1][0]>=1:
            nch2=matrix[list1[1][0]-1][list1[1][1]]
        else:
            nch2=matrix[5][list1[1][1]]
    else:
        nch1=matrix[list1[0][0]][list1[1][1]]
        nch2=matrix[list1[1][0]][list1[0][1]]
    temp.append(nch1)
    temp.append(nch2)
    temp.reverse()
    declist.append(temp)

decrypted=''
for arr in declist:
    decrypted=decrypted+arr[1]+arr[0]
print("Decrypted : ",decrypted)
