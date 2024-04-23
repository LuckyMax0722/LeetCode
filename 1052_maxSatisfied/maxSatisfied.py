class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = [0, 0]
        max_s1 = 0

        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s[g] += c

            if i >= minutes:
                if grumpy[i - minutes]:
                    s[1] -= customers[i - minutes]

            max_s1 = max(max_s1, s[1])

        return s[0] + max_s1

        '''
        def hadamard_product(v1, v2):
            return [x * y for x, y in zip(v1, v2)]

        grumpy = [x ^ 1 for x in grumpy]

        output = hadamard_product(customers, grumpy)
        ans = 0

        for i in range(len(customers) - minutes + 1):
            ans = max(ans, sum(output[:i]) + sum(customers[i:i + minutes]) + sum(output[i + minutes:]))

        return ans
        #超时
        '''

        '''
        def hadamard_product(v1, v2):
            return [x * y for x, y in zip(v1, v2)]
        ans = 0

        for i in range(len(customers) - minutes + 1):
            temp = copy.deepcopy(grumpy)
            temp[i: i + minutes] = [1] * minutes
            ans = max(ans, sum(hadamard_product(customers, temp)))

        return ans
        #超时
        '''