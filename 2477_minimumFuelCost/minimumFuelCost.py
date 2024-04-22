class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = [[] for _ in range(len(roads) + 1)]

        for x, y in roads:
            g[x].append(y)
            g[y].append(x)

        self.ans = 0

        def dfs(x, fa):
            size = 1

            for i in g[x]:
                if i != fa:
                    size += dfs(i, x)

            if x:
                self.ans += ceil(size / seats)

            return size

        dfs(0, -1)
        return self.ans