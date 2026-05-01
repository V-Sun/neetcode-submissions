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
        if not head or not head.next:
            return
        dummy = ListNode(-1, head)

        slow = head
        fast = head


        slow = head
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse(slow)
        fast = dummy.next


        while slow and fast:
            temp1 = fast.next
            temp2 = slow.next
            fast.next = slow
            slow.next = temp1
            fast = temp1
            slow = temp2

        if fast:
            fast.next = None


    

    