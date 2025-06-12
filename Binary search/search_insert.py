nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
s = 0
e = len(nums) - 1
s=0
e=len(nums)-1
while s<=e:
    mid=(s+e)//2
    if(nums[mid]==target):
        print(mid)
    elif(nums[mid]<target):
        s=mid+1
    else:
        e=mid-1

print (s)
        