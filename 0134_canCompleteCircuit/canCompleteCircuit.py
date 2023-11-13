class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        reamin_gas = [0 for _ in range(len(gas) + 1)]
        min_reamin_gas = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            reamin_gas[i + 1] = reamin_gas[i] + gas[i] - cost[i]

        min_reamin_gas_idx = reamin_gas.index(min(reamin_gas))

        return min_reamin_gas_idx

        # 图解法
        # 先遍历一次，检查剩余燃油情况
        # 找出最低点的天，也就是燃油亏空最严重的那天
        # 后一天就是解，因为亏空要靠之前的补齐
