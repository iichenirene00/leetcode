'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict={}
        for i in range(len(nums)):
            if(nums[i] in dict):
                return True
            dict[nums[i]]=1
        return False
        #time complexity: O(n)


q217=Solution()
print(q217.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))