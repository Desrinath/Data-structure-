n=[1,10,11,5,0]
s=0
e=len(n)-1
p=0
while s<=e:
    m=(s+e)//2
    if(n[m]>n[m+1]):
        p=m
        e=m-1
    else:
        s=m+1
print(p)
        
        