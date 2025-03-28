'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u']
        sv = []
        for i in range(len(s)):
            if s[i].lower() in vowel:
                sv.append(s[i])
        sv = sv[::-1]
        count = 0
        ss = list(s)
        for i in range(len(ss)):
            if ss[i].lower() in vowel:
                ss[i] = sv[count]
                count+=1
        return ''.join(ss)
        #time complexcity:O(n)
        
q345 = Solution()
print(q345.reverseVowels("IceCreAm"))