'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # dict = {}
        # for i in range(len(nums)+1):
        #     dict[i] = 0
        #     if(i in nums):
        #         dict[i] +=1
        # for k,v in dict.items():
        #     if (v==0):
        #         return k
        #time complexity:O(n)

        return (len(nums) * (len(nums) + 1))//2 - sum(nums)
        #time complexity: O(n)
    
q268 = Solution()
print(q268.missingNumber([9,6,4,2,3,5,7,0,1]))
    