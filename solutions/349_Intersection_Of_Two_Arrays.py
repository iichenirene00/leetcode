'''
Given two integer arrays nums1 and nums2, return an array of their 
intersection
Each element in the result must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # count = {}
        # for i in range(len(nums1)):
        #     if(nums1[i] in count):
        #         count[nums1[i]] += 1
        #     else:
        #         count[nums1[i]] = 1
        # intersect = set()
        # for j in range(len(nums2)):
        #     if nums2[j] in count:
        #         intersect.add(nums2[j])
        # return list(intersect)
        #time complexity: O(m+n)

        count = {}
        for num in nums1:
            count[num] = count.get(num,0)+1
        ans = []
        for num in nums2:
            if num in count:
                ans.append(num)
                del count[num]
        return ans
        #time complexity: O(m+n)
q349 = Solution()
print(q349.intersection([4,9,5],[9,4,9,8,4]))