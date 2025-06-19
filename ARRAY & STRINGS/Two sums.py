
#TWO SUMS 

#1) Brute force 

'''def two(nums,target ):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]
nums=[2,7,6,2]
target=7
r=two(nums,target)
print(r)'''

# 2) optimal approach using the Hash map 

''' 💡 Let’s Build Intuition
🧠 Think of this like a puzzle:
You’re walking through the array. At each number:

You ask:

“If I want to reach target, what do I need to pair with this number?”

You check:

“Have I already seen that ‘needed number’ earlier?”

If YES → You've got your answer.
If NO → Store this number and its index in a hash map and move on'''

#code 

def twosum(nums,target):
    num_map={}
    #to store number and its index

    for i,num in enumerate(nums):
        c=target-num

        if c in num_map:
            return[num_map[c],i]
        
        num_map[num]=i

nums=[2,7,6,2]
target=7
r=twosum(nums,target)
print(r)
