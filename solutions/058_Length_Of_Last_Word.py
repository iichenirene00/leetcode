'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split()
        return len(s[-1])
        #time complexcity:O(n)

q58 = Solution()
print(q58.lengthOfLastWord("   fly me   to   the moon  "))