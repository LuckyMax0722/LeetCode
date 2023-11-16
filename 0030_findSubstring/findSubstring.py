from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        """
        n = len(words[0])
        l,r = (0, 0)
        ans = []
        temp = words[:]
        sub_s = []

        while r + n <= len(s):
            if s[r:r+n] in temp:
                sub_s.append(s[r:r+n])
                temp.remove(s[r:r+n])
                r = r + n
            elif s[r:r+n] not in temp and not temp:
                ans.append(l)
                temp = words[:]
                sub_s = []
                print(s[r:r+n])
                sub_s.append(s[r:r+n])
                temp.remove(s[r:r+n])
                l = r
                r = r + n
            elif s[r:r+n] not in temp and temp:
                while True:
                    temp.append(sub_s[0])
                    sub_s = sub_s[1:]

                    if s[r:r+n] in temp:
                        sub_s.append(s[r:r+n])
                        temp.remove(s[r:r+n])
                        r = r + n
                        break


        print(ans)

        # 我的笨蛋想法
        """

        if not s or not words: return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []

        for i in range(n - all_len + 1):
            tmp = s[i:i + all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j + one_word])

            if Counter(c_tmp) == words:
                res.append(i)
        return res

        # 恒定窗口大小，检查每一个窗口 +1
        # 算了，思路2的太复杂了
        # 我的小脑袋瓜也想不出来

