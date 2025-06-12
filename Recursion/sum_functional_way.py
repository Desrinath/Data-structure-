def suum(n):
    if(n==0):
        return 0
    return n+suum(n-1)

n=int(input("enter the number :"))
print(suum(n))