Ini_Per = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

def binvalue(val, bitsize): 
    if val=='A' or val=='a':
        val=10
    if val=='B' or val=='b':
        val=11
    if val=='C' or val=='c':
        val=12
    if val=='D' or val=='d':
        val=13
    if val=='E' or val=='e':
        val=14
    if val=='F' or val=='f':
        val=15
    val=int(val)
    binval = bin(val)[2:]
    while len(binval) < bitsize:
        binval = "0"+binval 
    return binval

def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    if(decimal==10):
      decimal='A'  
    if(decimal==11):
      decimal='B'  
    if(decimal==12):
      decimal='C'  
    if(decimal==13):
      decimal='D'  
    if(decimal==14):
      decimal='E'  
    if(decimal==15):
      decimal='F'  
    return decimal

def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

def expand(block, table):
    return [block[x-1] for x in table]

def substitute(d_e):
    subblocks = nsplit(d_e, 6)
    result = list()
    for i in range(len(subblocks)): 
        block = subblocks[i]
        row = int(str(block[0])+str(block[5]),2)
        column = int(''.join([str(x) for x in block[1:][:-1]]),2) 
        val = S_BOX[i][row][column] 
        bin = binvalue(val, 4)
        result += [int(x) for x in bin]
    return result

def permut(block, table):
        return [block[x-1] for x in table]


plain= "123456ABCD132536"
key = "AABB09182736CCDD"

plain_bin=''
for ch in plain:
    plain_bin+=binvalue(ch,4)

Ini_Permuted_Plain=''
for i in Ini_Per:
    Ini_Permuted_Plain+=plain_bin[i-1]

After_Ini_Permute=''
plains=nsplit(Ini_Permuted_Plain,4)
for i in range(len(plains)):
    After_Ini_Permute+=str(binaryToDecimal(int(plains[i])))
#print(After_Ini_Permute)

round_keys=[['194CD072DE8C'],['4568581ABCCE'],['06EDA4ACF5B5'],['DA2D032B6EE3'],['69A629FEC913'],['C1948E87475E'],['708AD2DDB3C0'],['34F822F0C66D'],['84BB4473DCCC'],['02765708B5BF'],['6D5560AF7CA5'],['C2C1E96A4BF3'],['99C31397C91F'],['251B8BC717D0'],['3330C5D9A36D'],['181C5D75C66D']]

l=[]
r=[]
l.append(After_Ini_Permute[:8])
r.append(After_Ini_Permute[8:])

for c in range(16):
    rstr=''    
    for ch in r[c]:
        ch1=binvalue(ch,4)
        rstr+=ch1
    t=expand(rstr,E)
    t1=''
    for ch in t:
        t1+=str(ch)
    rkeystr=''
    for str1 in round_keys[0]:
        for ch in str1:
            ch1=binvalue(ch,4)
            rkeystr+=str(ch1)
    t2=rkeystr
    t=''
    for i in range(len(t1)):
        t+=str(int(t1[i])^int(t2[i]))
    #print(t)
    tarr=[]
    for ch in t:
        tarr.append(ch)
    #print(tarr)
    subarr=substitute(tarr)
    #print(subarr)
    tmp = permut(subarr, P)
    #print(tmp)
    tmp1=''
    for ch in tmp:
        tmp1+=str(ch)
    lstr=''
    for ch in l[c]:
        ch1=binvalue(ch,4)
        lstr+=ch1
    sp_text = ''
    for i in range(len(tmp1)):
        sp_text+=str(int(tmp1[i])^int(lstr[i]))
    #print(sp_text)
    tfinal=''
    texts=nsplit(sp_text,4)
    for i in range(len(texts)):
        tfinal+=str(binaryToDecimal(int(texts[i])))
    #print(tfinal)
    rnew=tfinal
    lnew=r[c]
    l.append(lnew)
    r.append(rnew)
    print("l["+str(c)+"] --> "+str(rnew))
    print("r["+str(c)+"] --> "+str(lnew))









