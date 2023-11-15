class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_ASCII = ''.join(str for str in s if str.isalnum())

        if s_ASCII.upper() == s_ASCII[::-1].upper():
            return True
        else:
            return False
