n=5
base=5
ans=0
while(n>0):
    last=(n&1)
    n=n>>1
    ans+=last+base
    base=base*5
print(ans)