'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}

        for a in s:
            mp[a] = mp.get(a, 0) + 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i

        return -1
        #time complexcity:O(n)

q387 = Solution()
print(q387.firstUniqChar("loveleetcode"))