# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        cur = dummy = ListNode() # dummy 节点是哨兵节点，不能向空节点的末尾添加节点
        up = 0

        while l1 or l2 or up:
            output = (l1.val if l1 else 0) + (l2.val if l2 else 0) + up

            cur.next = ListNode(output % 10)  # 向该链表末尾添加一个节点
            up = output // 10

            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next  # 哨兵节点的下一个节点就是最终要返回的链表头节点