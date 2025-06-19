'''
Given:
An integer array nums.

Task:
Return True if any value appears at least twice in the array, and False if every element is distinct.

🔸 Example:
Input: nums = [1, 2, 3, 4]
Output: False

Input: nums = [1, 2, 3, 1]
Output: True

BRUTE FORCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def dup(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]
                return TRUE 
    return False 
'''

#optimal
'''
🔍 Key Idea:
As you scan the array:

Keep a set of seen elements

If the current number is already in the set, return True

Otherwise, add it to the set and continue

Input: nums = [3, 1, 4, 2, 5, 3]

Step	num	    seenset	            Action
0	    3	    {}	                Add 3
1	    1	    {3}	                Add 1
2	    4	    {1, 3}	            Add 4
3	    2	    {1, 3, 4}	        Add 2
4	    5	    {1, 2, 3, 4}    	Add 5
5	    3	    {1, 2, 3, 4, 5}	    3 is already there → ✅ Return True
'''
def duplicate(nums):
    seen =set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
nums=[1, 2, 3, 4,4]
a=duplicate(nums)
print(a)