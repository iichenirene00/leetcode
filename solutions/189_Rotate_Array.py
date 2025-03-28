'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
        return nums
        #time complexcity:O(n)

q189 = Solution()
print(q189.rotate([1,2,3,4,5,6,7],3))