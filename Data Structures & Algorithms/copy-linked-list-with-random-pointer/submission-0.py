"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        random = {}
        old_to_new = {}

        temp = head
        copy = Node(-1)
        iter = copy
        while temp is not None:
            iter.next = Node(temp.val)
            iter = iter.next
            old_to_new[temp] = iter
            temp = temp.next
        
        temp = head
        iter = copy.next
        while iter != None:
            if temp.random is not None:
                iter.random = old_to_new[temp.random]
            else:
                iter.random = None
            iter = iter.next
            temp = temp.next
        
        return copy.next

        
        