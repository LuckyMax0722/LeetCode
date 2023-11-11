class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = max(prices)
        max_profit = 0

        for idx in range(len(prices)):
            if prices[idx] < min_price:
                min_price = prices[idx]
            elif (prices[idx] - min_price) > max_profit:
                max_profit = prices[idx] - min_price

        return max_profit

        # 动态规划
        # 把最高值设成最低价
        # 然后开始遍历
        # 比最低价 低 就设置成 最低价
        # 比最低价 高 就比较利润



