class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        '''
        candidates.sort()
        path = []
        ans = []
        n = len(candidates)

        def backtrack(candidates, begin, n, path, ans, target):
            if target == 0:
                if path not in ans:
                    ans.append(path)
                return
            elif target < 0:
                return

            for i in range(begin, n):
                backtrack(candidates, i + 1, n, path + [candidates[i]], ans, target - candidates[i])


        backtrack(candidates, 0, n, path, ans, target)
        return ans
        # 超时
        '''

        candidates.sort()
        n = len(candidates)
        ans = []

        def dfs(begin, path, res):
            if res == 0:
                ans.append(path[:])
                return

            for i in range(begin, n):
                if candidates[i] > res:
                    break

                if i > begin and candidates[i - 1] == candidates[i]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, path, res - candidates[i])
                path.pop()

        dfs(0, [], target)
        return ans
