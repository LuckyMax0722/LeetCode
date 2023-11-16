from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        """
        if len(s) < len(t): return ''

        hash = Counter(t)

        for windows_len in range(len(t), len(s) + 1):
            for idx in range(len(s) - windows_len + 1):
                if all(Counter(s[idx: idx + windows_len])[key] >= value for key, value in hash.items()):
                    return s[idx: idx + windows_len]

        return ''

        # 又超时了
        """

        """
        if len(s) < len(t): return ''

        l, r = (0, 0)
        ans = ''
        hash = Counter(t)

        while r < len(s):            
            if all(Counter(s[l:r+1])[key] >= value for key, value in hash.items()):
                if not ans:
                    ans = s[l:r+1]
                if len(s[l:r+1]) < len(ans):
                    ans = s[l:r+1]
                l = l + 1
            else:
                r = r + 1

        return ans

        # 又超时了
        """

        need = Counter(t)

        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1  # hash表会是负的，没有的key会创建出来

            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素

                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1

                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果

