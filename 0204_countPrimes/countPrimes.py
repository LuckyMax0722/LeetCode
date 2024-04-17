from collections import Counter


class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0:
            return 0
        else:

            prime = [True] * (n + 1)
            prime[0], prime[1] = False, False

            p = 2

            while (p * p <= n):
                if prime[p] == True:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                p += 1
        return Counter(prime[:-1])[True]

        # 2433ms

        '''
        if n == 0:
            return 0
        else:
            prime = [True] * (n + 1)
            prime[0], prime[1] = False, False

            primes = []

            for i in range(2, n):
                if prime[i]:
                    primes.append(i)
                for p in primes:
                    if i * p >= n:
                        break
                    prime[i * p] = False

                    if i % p == 0:
                        break
        # 2433ms
        return len(primes)
        '''

