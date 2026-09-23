# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersRecursive(l1, l2)
        # return self.addTwoNumbersIterative(l1, l2)

    def addTwoNumbersRecursive(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        # dummy = ListNode(-1)
        # current = dummy
        # carry = 0
        # while l1 or l2 or carry:
        l1_val = 0
        if l1:
            l1_val = l1.val
            l1 = l1.next

        l2_val = 0
        if l2:
            l2_val = l2.val
            l2 = l2.next

        digit_sum = l1_val + l2_val + carry # sum can only take 2 arguements
        node_Val = digit_sum % 10
        carry = int(digit_sum / 10)

        node = ListNode(node_Val)
        nxt = None
        if l1 or l2 or carry: 
            nxt = self.addTwoNumbersRecursive(l1, l2, carry)
        node.next = nxt
        return node

    def addTwoNumbersIterative(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = 0
            if l1:
               l1_val = l1.val
               l1 = l1.next

            l2_val = 0
            if l2:
               l2_val = l2.val
               l2 = l2.next

            digit_sum = l1_val + l2_val + carry # sum can only take 2 arguements
            node_Val = digit_sum % 10
            carry = int(digit_sum / 10)

            node = ListNode(node_Val)
            current.next = node
            current = node 


        return dummy.next


