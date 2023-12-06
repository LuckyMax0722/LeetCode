class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        string = "1"

        def process(string):
            last_s = ""
            count = 0
            temp_string = ""

            for i, s in enumerate(string[::-1]):
                if i == 0:
                    last_s = s
                    count = count + 1
                    temp_string = temp_string + s
                else:
                    if last_s == s:
                        count = count + 1
                    else:
                        temp_string = temp_string + str(count)
                        last_s = s
                        count = 1
                        temp_string = temp_string + s

            temp_string = temp_string + str(count)

            return temp_string[::-1]

        for _ in range(n - 1):
            string = process(string)

        return string
