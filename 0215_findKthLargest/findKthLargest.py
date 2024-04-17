class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        sorted_list = sorted(nums)
        return sorted_list[-k]

        # 内置排序
        '''

        '''
        pq = []

        for num in nums:
            heapq.heappush(pq, num)

            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]

        # 堆超时
        '''

        return heapq.nlargest(k, nums)[-1]