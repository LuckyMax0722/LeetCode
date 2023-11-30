class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        '''
        m = len(grid) - 1 # 行
        n = len(grid[0]) - 1 # 列

        node_list = [[0, 0, grid[0][0]]]
        cur = []

        def BestFirstSearch(cur_node):
            if cur_node[0] == m:
                node_list.append([cur_node[0], cur_node[1] + 1, cur_node[2] + grid[cur_node[0]][cur_node[1] + 1]])
            elif cur_node[1] == n:
                node_list.append([cur_node[0] + 1, cur_node[1], cur_node[2] + grid[cur_node[0] + 1][cur_node[1]]])
            else:
                node_list.append([cur_node[0] + 1, cur_node[1], cur_node[2] + grid[cur_node[0] + 1][cur_node[1]]])
                node_list.append([cur_node[0], cur_node[1] + 1, cur_node[2] + grid[cur_node[0]][cur_node[1] + 1]])

        def FindMinCost(all_node):
            min_index, cur = min(enumerate(node_list), key=lambda x: x[1][2])
            node_list.pop(min_index)
            return cur


        while True:
            cur = FindMinCost(node_list)

            if cur[0] == m and cur[1] == n:
                return cur[2]
            else:
                BestFirstSearch(cur)

        # 超时 
        '''

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

        # 动态规划 每个位置都基于之前的和现在的更新
