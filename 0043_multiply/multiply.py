class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        dict = {"1":1, "2":2, "3":3 , "4":4 , "5":5, "6":6 , "7":7, "8":8, "9":9, "0":0}

        num1_int, num2_int = 0, 0

        for i, s in enumerate(num1[::-1]):
            num1_int = num1_int + dict[s] * (10 ** i)

        for i, s in enumerate(num2[::-1]):
            num2_int = num2_int + dict[s] * (10 ** i)

        return str(num1_int * num2_int)