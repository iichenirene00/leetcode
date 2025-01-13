'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        seen = {}
        for i in range(len(nums)):
            if(nums[i] in seen):
                seen[nums[i]] += 1
            else:
                seen[nums[i]]=1
        for k,v in seen.items():
            if v==1:
                return k
        #time compexity: O(n)

q136 = Solution()
print(q136.singleNumber([4,1,2,1,2]))