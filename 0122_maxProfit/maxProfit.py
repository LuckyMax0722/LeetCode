class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        buy_price = prices[0]
        last_day_price = prices[0]

        profit = 0
        total_profit = 0

        for idx in range(len(prices)):
            if prices[idx] < last_day_price:
                last_day_price = prices[idx]
                buy_price = prices[idx]
                total_profit = total_profit + profit
                profit = 0
            elif prices[idx] >= last_day_price:
                if idx != len(prices) - 1:
                    last_day_price = prices[idx]
                    profit = prices[idx] - buy_price
                elif idx == len(prices) - 1:
                    profit = prices[idx] - buy_price
                    total_profit = total_profit + profit

        return total_profit

        # 自己想的笨办法
        """

        total_profit = 0

        last_day_price = prices[0]
        for idx in range(len(prices)):
            if prices[idx] >= last_day_price:
                total_profit = total_profit + prices[idx] - last_day_price
                last_day_price = prices[idx]
            else:
                last_day_price = prices[idx]

        return total_profit

        # 贪心算法