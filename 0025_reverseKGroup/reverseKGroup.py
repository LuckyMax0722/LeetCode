# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = cur = ListNode()

        while True:
            count = k
            stack = []
            tmp = head

            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1

                # 把节点放入临时栈中
                # 如果不够数量会跳出

            if count:
                cur.next = head
                break

            while stack:
                cur.next = stack.pop()
                cur = cur.next

            cur.next = tmp
            head = tmp

        return dummy.next

