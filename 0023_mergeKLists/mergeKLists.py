# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, idx, node))

        dummy = ListNode()
        current = dummy

        while pq:
            val, idx, node = heapq.heappop(pq)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))

        return dummy.next