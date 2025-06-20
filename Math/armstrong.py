n=153
n2=n
temp=n
count=0

while temp>0:
    temp=temp//10
    count+=1


sum=0
while n>0:
    d=n%10
    sum=sum+d**count
    n=n//10



if(sum==n2):
    print("yes armstrong number")
else:
    print("not a armstrong number ")
