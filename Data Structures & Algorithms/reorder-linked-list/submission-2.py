# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, node):
        prev = None
        cur = node

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(-1, head)
        
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        temp = slow.next
        slow.next = None
        slow2 = self.reverse(temp)
        slow = head

        while slow and slow2:
            temp1 = slow.next
            temp2 = slow2.next

            slow.next = slow2
            slow2.next = temp1

            slow = temp1
            slow2 = temp2
        

            

        
        

        

    

    