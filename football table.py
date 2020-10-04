num=int(input())
x = (num*(num-1))//2
table=dict()
for i in range(x):
    inpstr=input().split()
    valTemp=0
    if(int(inpstr[2])>int(inpstr[4])):
        if(inpstr[0] in table.keys()):
            
            valTemp=int(table.get(inpstr[0]))+3
            table.update({inpstr[0]:valTemp})
        else:
            table.update({inpstr[0]:3})
        
    else:
        if(inpstr[0] in table.keys()):
            
            valTemp=int(table.get(inpstr[0]))+0
            table.update({inpstr[0]:valTemp})
        else:
            table.update({inpstr[0]:0})
        
    if(int(inpstr[2])<int(inpstr[4])):
        if(inpstr[1] in table.keys()):
            
            valTemp=int(table.get(inpstr[1]))+3
            table.update({inpstr[1]:valTemp})
        else:
            table.update({inpstr[1]:3})
    else:
        if(inpstr[1] in table.keys()):
            
            valTemp=int(table.get(inpstr[1]))+0
            table.update({inpstr[1]:valTemp})
        else:
            table.update({inpstr[0]:0})
            
    if(int(inpstr[2])==int(inpstr[4])):
        if(inpstr[0] in table.keys()):
            
            valTemp=int(table.get(inpstr[0]))+1
            table.update({inpstr[0]:valTemp})
            
        else:
            table.update({inpstr[0]:1})
            
        if(inpstr[1] in table.keys()):
            
            valTemp=int(table.get(inpstr[1]))+1
            table.update({inpstr[1]:valTemp})
            
        else:
            table.update({inpstr[1]:1})    
  
maxval=0  
team=''
for k in table.keys():
    if(table.get(k)>maxval):
        maxval=table[k]
        team=k
print(team)
print(maxval)
