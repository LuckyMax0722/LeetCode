class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        ans = []
        tmp = ""

        def dfs(digits, ans, tmp):
            if not digits:
                if len(tmp) != 0: ans.append(tmp)
                return

            for _, str in enumerate(dict[digits[0]]):
                tmp = tmp + str
                dfs(digits[1:], ans, tmp)
                tmp = tmp[:-1]


        dfs(digits, ans, tmp)

        return ans
