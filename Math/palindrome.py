n=1234
rev=0

while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)

if(n==rev):
    print("palindrome")
else:
    print("not a palindrome")