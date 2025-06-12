def pal(i,n,s):
    if(i>=n//2):
        return True
    if(s[i]!=s[n-i-1]):
        return False
    return pal(i+1,n,s)

s="MADA"
i=0
n=len(s)
print(pal(i,n,s))
