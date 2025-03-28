'''
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount
'''

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices
        #time complexcity:O(n^2)

q1475 = Solution()
print(q1475.finalPrices([8,4,6,2,3]))