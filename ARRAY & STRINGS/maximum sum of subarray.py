def Arrayyy(nums):
    current=nums[0]
    max=nums[0]

    for i in range(1,len(nums)):
        num=nums[i]
        
        if current+num>num:
            current=current+num
        else:
            current=num
        if current>max:
            max=current
    return max

nums=[1,-2,3,4,5,6,7-4,-3]
print(Arrayyy(nums))