n=27
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if (sum==n):
    print("perfect")
else:
    print("not a perfect")