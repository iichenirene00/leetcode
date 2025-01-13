'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # s = ''.join(str(x) for x in digits)
        # s = int(s)+1
        # s = [int(i) for i in str(s)]
        # return s
        # time complexity: O(n)

        for i in range(len(digits)-1,-1,-1):
            if(digits[i]==9):
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1]+digits
        # time complexity: O(n)

q66 = Solution()
print(q66.plusOne([9,9,9]))