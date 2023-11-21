class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        str_n = str(n)
        count = 0
        hash = {}

        while count < 100:
            sum = 0

            for i in range(len(str_n)):
                sum = sum + int(str_n[i]) * int(str_n[i])

            if sum == 1:
                return True
            elif sum not in hash:
                hash[sum] = n
            else:
                return False

            str_n = str(sum)
            count = count + 1