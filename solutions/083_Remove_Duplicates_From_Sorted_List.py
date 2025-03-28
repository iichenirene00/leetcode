'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        seen =[]
        pre = None
        cur = head
        while cur:
            if(cur.val not in seen):
                seen.append(cur.val)
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return head
        #time complexcity:O(n)
q83 = Solution()
print(q83.deleteDuplicates([1,1,2]))