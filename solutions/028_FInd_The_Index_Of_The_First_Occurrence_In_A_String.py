'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle not in haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1       
    #time complexcity:O(n)
q28 = Solution()
print(q28.strStr("sadbutsad","sad"))