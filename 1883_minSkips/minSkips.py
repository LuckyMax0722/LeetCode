class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) / speed > hoursBefore:
            return -1
        f = [0] * len(dist)
        for i in count(0):
            pre = 0
            for j, d in enumerate(dist[:-1]):
                tmp = f[j + 1]
                f[j + 1] = (f[j] + d + speed - 1) // speed * speed
                if i:
                    f[j + 1] = min(f[j + 1], pre + d)
                pre = tmp
            if f[-1] + dist[-1] <= speed * hoursBefore:
                return i
