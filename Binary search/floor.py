nums =[10,12,14,16,20]
target = 15
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

print (nums[e])
        