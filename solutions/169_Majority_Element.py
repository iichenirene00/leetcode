'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if(nums[i]in count):
                count[nums[i]]+=1
            else:
                count[nums[i]] =1
        max = len(nums)//2
        for k,v in count.items():
            if(v > max):
                return k
        #time complexity:O(n)
q169 = Solution()
print(q169.majorityElement([2,2,1,1,1,2,2]))