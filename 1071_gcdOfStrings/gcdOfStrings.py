class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        # 定义一个递归函数来计算最大公约数
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        # 通过切片返回最大公约数长度的字符串
        return str1[:gcd(len(str1), len(str2))]