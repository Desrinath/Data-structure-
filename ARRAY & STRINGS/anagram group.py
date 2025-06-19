def grou(s):
    ana={}
    for word in s:
        c=[0]*26
        for cha in word:
            c[ord(cha)-ord('a')]+=1
        key=tuple(c)

        if key not in ana:
            ana[key]=[word]
        else:
            ana[key].append(word)
    return list(ana.values())
s=["eat", "tea", "tan", "ate", "nat", "bat"]
print(grou(s))