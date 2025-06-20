a=3
ba=5
b=a
result=1
while b>0:
    if b&1:
        result=result*ba
    ba=ba*ba
    b=b>>1
print(result)