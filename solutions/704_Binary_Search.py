'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)-1 #keep track of what part of list I'm searching
        while low<=high: #while haven't narrow down to one element
            mid = (low+high)//2 #check from the middle
            guess = nums[mid] #the number we're guessing
            if guess ==target:
                return mid
            elif guess > target: #the guessing is too high
                high = mid-1
            else: #the guessing is too low
                low = mid+1
        return -1
        #the target is not inside the list

#TimeComplexity:O(logn)

q704 = Solution()
print(q704.search([-1,0,3,5,9,12],9))