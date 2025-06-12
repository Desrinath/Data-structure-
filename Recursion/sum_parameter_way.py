def suum(n,s):
    if(n<1):
        print(s)
        return
    suum(n-1,s+n)
    

n=int(input("enter the number :"))
s=0
suum(n,s)