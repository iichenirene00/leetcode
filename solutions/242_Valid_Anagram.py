'''
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if(s[i] in seen_s):
                seen_s[s[i]]+=1
            else:
                seen_s[s[i]]=1
        
        for i in range(len(t)):
            if(t[i] in seen_s):
                seen_s[t[i]]-=1
            else:
                return False
        for val in seen_s.values():
            if val != 0: 
                return False
        return True
        #time complexcity:O(n)

q242=Solution()
print(q242.isAnagram( "anagram","nagaram"))