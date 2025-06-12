def rev(i,arr,n,a):
    if(i>=a):
        return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    rev(i+1,arr,n,a)

arr=[1,2,3,4,5]
n=len(arr)
a=n//2
i=0
rev(i,arr,n,a)
print(arr)