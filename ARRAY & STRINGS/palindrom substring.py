def pal(s):
    r=''
    
    for i in range(len(s)):

        odd=palin(s,i,i)
        if len(odd)>len(r):
            r=odd
        even=palin(s,i,i+1)
        if len(even)>len(r):
            r=even
    return r
def palin(s,left,right):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1

    return s[left+1:right]
s='nabbam'
print(pal(s))
