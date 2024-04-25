class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        if n > 0:
            return (pow(3, round(log(n, 3))) == n)
        return False
        '''

        if n == 1 or n == 3 or n == 9 or n == 27 or n == 81 or n == 243 or n == 729 or n == 2187 or n == 6561 or n == 19683 or n == 59049 or n == 177147 or n == 531441 or n == 1594323 or n == 4782969 or n == 14348907 or n == 43046721 or n == 129140163 or n == 387420489 or n == 1162261467:
            return True
        else:
            return False
