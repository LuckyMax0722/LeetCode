class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, k, target, path, res):
            if k == 0 and target == 0:
                res.append(path)
                return
            if k == 0 or target <= 0:
                return
            for i in range(start, 10):
                backtrack(i + 1, k - 1, target - i, path + [i], res)

        res = []
        backtrack(1, k, n, [], res)
        return res