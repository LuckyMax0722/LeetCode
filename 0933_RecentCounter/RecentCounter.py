class RecentCounter(object):
    '''
    def __init__(self):
        self.ping_list = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ping_list.append(t)

        boundary = t - 3000

        while True:
            if self.ping_list[0] < boundary:
                self.ping_list.pop(0)
            else:
                return len(self.ping_list)


    '''
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)