"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        '''
        ans = copy.deepcopy(head)
        return ans
        # 深拷贝
        '''

        if not head: return

        hash = {}
        cur = head

        while cur:
            hash[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            hash[cur].next = hash.setdefault(cur.next)
            hash[cur].random = hash.setdefault(cur.random)
            cur = cur.next

        return hash[head]


