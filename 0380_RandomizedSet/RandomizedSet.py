import random

'''
class RandomizedSet(object):

    def __init__(self):
        self.RandomizedSet = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.RandomizedSet:
            return False
        else:
            self.RandomizedSet.append(val)
            return True


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.RandomizedSet:
            self.RandomizedSet.remove(val)
            return True
        else:
            return False



    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.RandomizedSet)

# O(n)复杂度
'''


class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.idx = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.idx:
            return False
        else:
            self.idx[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.idx:
            i = self.idx[val]
            self.nums[i] = self.nums[-1]
            self.idx[self.nums[i]] = i

            self.nums.pop()
            del self.idx[val]
            # hash表里执行了删除操作
            # list里执行了一个互换，然后删除最后一个
            # 神奇
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()