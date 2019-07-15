p = int(input("Enter p (prime) "))    
#g = 5      

allnum=[]
for i in range(1,p+1):
    allnum.append(i)

genlist=[]
for i in range(2,p-1):
    temp=[]
    for j in range(1,p):
        temp.append((i**j)%p)
    for k in allnum:
        if(k not in temp):
            break
        else:        
            if(k==p-1):
                genlist.append(i)
            else:
                continue
print(genlist)
g=int(input("Enter generator (g) from above list"))
 
x = int(input("Enter x (Alice's private x) "))     
y = int(input("Enter y (Bob's private y) "))      

print( "Publicly Shared Variables:")
print( "    p: " , p )
print( "    g:  " , g )
 
R1 = (g**x) % p
print( "\n  Alice Sends Over Public Chanel (R1) : " , R1 )
 
R2 = (g ** y) % p
print("\n   Bob Sends Over Public Chanel (R2): ", R2 )
 
print( "Privately Calculated Shared Secret:" )

k1 = (R2 ** x) % p
print( "\n  Key computed by Alice (K1): ", k1 )
 
k2 = (R1 ** y) % p
print( "\n  Key computed by Bob (K2): ", k2 )
