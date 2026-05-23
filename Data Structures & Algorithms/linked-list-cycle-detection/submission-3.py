# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setNode = set()
        trav = head

        while trav:
         
            if trav in setNode:
                return True
            
            setNode.add(trav)
            trav = trav.next

        return False