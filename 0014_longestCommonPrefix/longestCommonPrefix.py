class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        """
        res = ""
        for tmp in zip(*strs):  # 打包
            tmp_set = set(tmp)  # 创建集合

            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break

        return res
        # python特性，内置zip和set
        """

        if not strs:
            return ""
        res = strs[0]
        i = 1

        while i < len(strs):
            while strs[i].find(res) != 0:  # 在每个位置查res，不一样就从尾巴减少单词
                res = res[0:len(res) - 1]

            i += 1
        return res

