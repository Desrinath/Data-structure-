def ana(s,t):
    if len(s)!=len(t):
        return False
    cs=[0]*26
    ct=[0]*26

    for i in range(len(s)):
        cs[ord(s[i])-ord('a')]+=1
        ct[ord(t[i])-ord('a')]+=1

    for i in range(26):
        if cs[i]!=ct[i]:
            return False
    return True
s='nagaram'
t='anagram'
print(ana(s,t))
