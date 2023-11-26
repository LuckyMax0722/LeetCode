# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        temp = []

        while head:
            temp.append(head.val)
            head = head.next

        temp[left - 1: right] = temp[left - 1: right][::-1]

        ans = dummy = ListNode()

        for i, num in enumerate(temp):
            ans.next = ListNode(temp[i])
            ans = ans.next

        return dummy.next


