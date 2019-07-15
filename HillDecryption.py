from HillEncryption import *

print("Ciphertext : ",ciphertext)
print("Key : ",key)

def det2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

if lkey==2:
    det=det2x2(keyindexmat)
elif lkey==3:
    a,b,c = keyindexmat[0]
    efhi = [x[1:] for x in keyindexmat[1:]]
    dfgi = [x[::2] for x in keyindexmat[1:]]
    degh = [x[0:2] for x in keyindexmat[1:]]
    det = (a * det2x2(efhi) - b * det2x2(dfgi) + c * det2x2(degh))


det=det%26
invdet=det
for i in range(200):
    if (det*i)%26==1:
        invdet=i
        break

#print(det)
#print(invdet)

#invmat=keyindexmat
#print(keyindexmat)

if lkey==2:
    invmat=[[0,0],[0,0]]
    t=invmat[0][0]
    invmat[0][0]=keyindexmat[1][1]
    invmat[1][1]=t
    invmat[0][1]=0-keyindexmat[0][1]
    invmat[1][0]=0-keyindexmat[1][0]
elif lkey==3:
    invmat=[[0,0,0],[0,0,0],[0,0,0]]
    
    invmat[0][0]=(keyindexmat[1][1]*keyindexmat[2][2])-(keyindexmat[1][2]*keyindexmat[2][1])
    invmat[0][1]=(-1)*((keyindexmat[1][0]*keyindexmat[2][2])-(keyindexmat[1][2]*keyindexmat[2][0]))
    invmat[0][2]=(keyindexmat[1][0]*keyindexmat[2][1])-(keyindexmat[1][1]*keyindexmat[2][0])
    invmat[1][0]=(-1)*((keyindexmat[0][1]*keyindexmat[2][2])-(keyindexmat[0][2]*keyindexmat[2][1]))
    invmat[1][1]=(keyindexmat[0][1]*keyindexmat[2][2])-(keyindexmat[0][2]*keyindexmat[2][1])
    invmat[1][2]=(-1)*((keyindexmat[0][0]*keyindexmat[2][1])-(keyindexmat[0][1]*keyindexmat[2][0]))
    invmat[2][0]=(keyindexmat[0][1]*keyindexmat[1][2])-(keyindexmat[1][1]*keyindexmat[0][2])
    invmat[2][1]=(-1)*((keyindexmat[1][2]*keyindexmat[0][0])-(keyindexmat[0][2]*keyindexmat[1][0]))
    invmat[2][2]=(keyindexmat[1][1]*keyindexmat[0][0])-(keyindexmat[1][0]*keyindexmat[0][1])
#print(invmat)

keyinvmat=invmat
for r in range(lkey):
    for c in range(lkey):
        keyinvmat[r][c]=invdet*invmat[r][c]
        keyinvmat[r][c]=keyinvmat[r][c]%26
keyinvmat = [[keyinvmat[j][i] for j in range(len(keyinvmat))] for i in range(len(keyinvmat[0]))] 
#print(keyinvmat)

keyinvmat=[[25,22],[1,23]]

D=[]
for n in range(noofmat):
    di=[]
    for r in range(0,lkey,1):
        temp=[]
        for c in range(0,1,1):
            temp.append(0)
        di.append(temp)
    ci=C[n]
    ki=keyinvmat
    for i in range(len(keyinvmat)):
        for j in range(len(ci[0])):
            for k in range(len(ci)):
                di[i][j]=di[i][j]+(int(keyinvmat[i][k])*int(ci[k][j]))
                di[i][j]=di[i][j]%26
    D.append(di)
print(D)

plain=''
for list1 in D:
    for list2 in list1:
        for t in list2:
            for entry in alphamat:
                if t==entry[1]:
                    ch=entry[0]
                    plain=plain+ch
print(plain)
