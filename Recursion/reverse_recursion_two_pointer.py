def rev(l,r,arr):
    if(l>=r):
        return
    arr[l],arr[r]=arr[r],arr[l]
    rev(l+1,r-1,arr)

arr=[1,2,3,4,5]
n=len(arr)
l=0
r=n-1
rev(l,r,arr)
print(arr)