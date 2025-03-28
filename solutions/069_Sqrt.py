'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        #edge case: if x=0
        if x==0:
            return 0
        left,right = 1,x
        while left<=right:
            mid = (left+right)//2
            if(mid**2==x):
                return mid
            elif(mid**2<x):
                left = mid+1
            else:
                right = mid-1
        return right
        # time complexity:O(logn)

q69 = Solution()
print(q69.mySqrt(8))