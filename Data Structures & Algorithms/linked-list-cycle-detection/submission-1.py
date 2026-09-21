# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.hasCycleWithPointers(head)

    def hasCycleWithPointers(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        hasCycle = False
        slow = head
        fast = head.next
        while slow and fast:
            if slow == fast:
                hasCycle = True
                break
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
        return hasCycle

    
    def hasCycleWithSet(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head
        hasCycle = False
        while current:
            if current in seen:
                hasCycle = True
                break
            seen.add(current)
            current = current.next
        
        return hasCycle