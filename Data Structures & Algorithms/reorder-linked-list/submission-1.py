# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None


        # head -> slow(mid) -> second -> fast -> None
        # head -> slow -> None

        # second -> temp ->...
        # x -> second(temp)
        
        
        # prev -> (None)
        # second -> prev (none)

        #None ← A ← B ← C    D → None
                #         ↑  ↑
                #      prev curr


        while second:
            tmp = second.next
            second.next = prev

            prev = second
            second = tmp

        first, second = head, prev


        while second:
            tem1,tem2 = first.next, second.next

            first.next = second
            second.next = tem1

            first,second = tem1,tem2





