f=open("text.txt")

nums=[]
chars=[]

ch=f.read(1)
while(ch):
    if ch.isalpha()==True:
        ch=ch.lower()
        chars.append(ch)
    if ch.isdigit()==True:
        nums.append(ch)
    ch=f.read(1)

nodupchars=[]
nodupnums=[]
for i in chars:
    if i not in nodupchars:
        nodupchars.append(i)
for i in nums:
    if i not in nodupnums:
        nodupnums.append(i)

freqlist=[]

for i in nodupchars:
    temp=[]
    c=chars.count(i)
    temp.append(i)
    temp.append(c)
    freqlist.append(temp)

for i in nodupnums:
    temp=[]
    c=nums.count(i)
    temp.append(i)
    temp.append(c)
    freqlist.append(temp)

print(freqlist)
