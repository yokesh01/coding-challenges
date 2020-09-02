size= int(input())
queue=list(input())
temp=0
a=list()
b=list()

for x in range(0,len(queue)):
    if(queue[x]=='-'):
        continue
    if(queue[x]=='A'):
        a.append(x)
        temp=x
        x=x-1
        if(x>=0):
            while(queue[x] == '-'):
                a.append(x)
                x=x-1
                if(x<0):
                    break
            
        x=temp
    if(queue[x]=='B'):
        b.append(x)
        temp=x
        x=x+1
        if(x<=len(queue)-1):
            while(queue[x] == '-'):
                b.append(x)
                x=x+1
                if(x>len(queue)-1):
                    break
   
        x=temp
a=set(a)
copy=list(a)
copy=set(copy)
print(copy)
b=set(b)
print(b)
l=list(a.intersection(b))
a.difference_update(b) 
b.difference_update(copy) 
acount=len(a)
bcount=len(b)
l.sort()
count=1
x=0
while(x+1<len(l)):
    if (l[x+1]==l[x]+1):
        count=count+1
    else:
        acount=acount+(count//2)
        bcount=bcount+(count//2)
        count=1
    x=x+1
acount=acount+(count//2)
bcount=bcount+(count//2)   
if(acount == bcount):
    print("Coalition government")
elif(acount>bcount):
    print('A')
else:
    print('B')
