class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        '''
        digits = ''.join(map(str, digits))
        digits = int(digits) + 1
        digits = str(digits)
        digits = [int(x) for x in digits]

        return digits
        # 取巧
        '''

        if digits[-1] == 9:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
            if digits[0] == 0:
                digits.insert(0, 1)
        else:
            digits[-1] += 1

        return digits