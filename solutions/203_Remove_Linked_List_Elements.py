'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        temp = ListNode(0,head)
        pre = temp
        while cur:
            if(cur.val == val):
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return temp.next
        #time complexcity:O(n)
q203 = Solution()
print(q203.removeElements([1,2,6,3,4,5,6],6))