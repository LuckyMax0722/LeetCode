# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = cur = ListNode()
        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        stack.pop(len(stack) - n)

        for _, num in enumerate(stack):
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next
