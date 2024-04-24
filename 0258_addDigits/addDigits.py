class Solution:
    def addDigits(self, num: int) -> int:
        '''
        temp = []

        if 0 <= num <= 9:
            return num
        else:
            while num:
                temp.append(num % 10)
                num = (num - num % 10) // 10
            return self.addDigits(sum(temp))

        '''

        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

