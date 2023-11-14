class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roam_dict_hundred = {100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC',
                             900: 'CM'}
        roam_dict_ten = {10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50.: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'}
        roam_dict_one = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5.: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        ans = ''

        thousand = num // 1000
        for _ in range(thousand):
            ans = ans + 'M'
        num = num - thousand * 1000

        hundred = num // 100
        if hundred * 100 in roam_dict_hundred:
            ans = ans + roam_dict_hundred[hundred * 100]
        num = num - hundred * 100

        ten = num // 10
        if ten * 10 in roam_dict_ten:
            ans = ans + roam_dict_ten[ten * 10]
        num = num - ten * 10

        if num in roam_dict_one:
            ans = ans + roam_dict_one[num]

        return ans
