from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        hash_table = Counter(changed)
        res = []

        for num in changed:
            if hash_table[num] == 0:
                continue
            hash_table[num] -= 1
            if hash_table[num * 2] == 0:
                return []
            hash_table[num * 2] -= 1
            res.append(num)

        return res
