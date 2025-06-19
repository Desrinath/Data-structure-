def chaa(s):
    cha=set()
    left=0
    maxx=0

    for right in range(len(s)):
        while s[right] in cha :
            cha.remove(s[left])
            left=left+1
        cha.add(s[right])
        maxx=max(maxx,right-left+1)
    return maxx
s='abcabcbb'
print(chaa(s))