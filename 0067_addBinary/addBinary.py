class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        carry = 0
        out = ''

        while a or b or carry:
            carry = (int(a[-1]) if a else 0) + (int(b[-1]) if b else 0) + carry

            out = str((carry % 2)) + out
            carry = carry // 2
            # 切片
            a = a[:-1]
            b = b[:-1]

        return out