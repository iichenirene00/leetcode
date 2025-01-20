'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
        f_v = count[s[0]]
        for v in count.values():
            if(f_v!=v):
                return False
        return True
        #time complexcity:O(n)

q1941 = Solution()
print(q1941.areOccurrencesEqual("abacbc"))