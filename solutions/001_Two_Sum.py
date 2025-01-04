class Solution:
    def twoSum(self, nums, target):
        # for i in range(len(nums)):
        #     if(target - nums[i] in nums and i!=nums.index(target - nums[i])):
        #         return [i, nums.index(target - nums[i])]
        # time complexity: O(n^2)

        # for i in range(len(nums)):
        #     for j in range (1,len(nums)):
        #         if(target-nums[i]==nums[j] and i!=j):
        #             return [i,j]
        # time complexity: O(n^2)

        sol = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if(remain in sol):
               return [sol[remain], i]
            else:
                sol[nums[i]]=i
        # time complexity: O(n)


case1 = Solution()
print(case1.twoSum([2,7,11,15],9))
