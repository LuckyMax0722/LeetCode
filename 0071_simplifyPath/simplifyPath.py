import os

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        return os.path.realpath(path)
        # realpath 返回标准的path