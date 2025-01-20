'''
Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.
'''

class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        # for index, value in enumerate(arr):
        #     if (index==value):
        #         return index 
        
        # return -1
        # time complexcity: O(n)
        
        left = 0
        right = len(arr)-1
        while (left<=right):
            mid = (left+right)//2
            if(arr[mid]==mid and not (mid and arr[mid-1]==mid-1)):
                return mid
            elif(arr[mid]<mid):
                left = mid+1
            else:
                right = mid-1
        return -1
        #time complexcity:O(logn)
    
q1064 = Solution()
print(q1064.fixedPoint([-10,-5,0,3,7]))