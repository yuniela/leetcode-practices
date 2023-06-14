# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode() # for edge cases
        current, carry = dummy, 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            carry, curr_value = divmod(val1 + val2 + carry, 10)
            current.next = ListNode(curr_value) # initially we add to dummy
            current = current.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return dummy.next