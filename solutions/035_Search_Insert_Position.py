'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums, target):
        left,right = 0, len(nums)-1 #index for first and last
        while left<=right:
            mid = (left+right)//2 #middle index
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                left = mid+1 #since mid index is smaller than target we don't need the left part
            else:
                right = mid-1 #if mid index is greater than target we don't need the right part
        return left
    # time complexity: O(logn)

q35 = Solution()
print(q35.searchInsert([1,3,5,6],2))