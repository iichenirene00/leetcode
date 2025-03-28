'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        list = []
        while head:
            list.append(head.val)
            head = head.next
        left = 0
        right = len(list)-1
        while left <right:
            if(list[left]!=list[right]):
                return False
            else:
                left+=1
                right-=1
        return True
        #time complexcity:O(n)

q234 = Solution()
print(q234.isPalindrome([1,2,2,1]))

