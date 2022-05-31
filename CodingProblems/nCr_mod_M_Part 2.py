# User function Template for python3

import math


class Solution:
    def binExp(self, a, b, mod):
        res = 1

        while b > 0:
            if b % 2 == 1:
                res = (res * a) % mod
                b -= 1
            a = (a * a) % mod
            b //= 2

        return res

    def findNcR(self, n, r, factorial, mod):
        if r > n:
            return 0

        if n == r:
            return 1

        return (((factorial[n] * self.binExp(factorial[int(n - r)], mod - 2, mod)) % mod) * self.binExp(factorial[r], mod - 2, mod)) % mod

    def baseConversion(self, a, b):
        # a to base b
        res = []

        while a > 0:
            res.append(a % b)
            a //= b

        return res

    def nCrModM(self, n, r, m):
        # Code here
        primeFactors = []
        factorial = [0] * m

        mod = m
        factorial[0] = 1

        for i in range(1, m):
            factorial[i] = (factorial[i - 1] * i) % mod

        for i in range(2, math.floor(math.sqrt(m))):
            if m % i == 0:
                primeFactors.append(i)
                while m % i == 0:
                    m //= i

        if m > 1:
            primeFactors.append(m)

        # print("primeFactors" + " " + str(primeFactors))

        numFactors = len(primeFactors)
        pp = [0] * numFactors
        invpp = [0] * numFactors
        ans = 0

        for i in range(numFactors):
            pp[i] = mod // primeFactors[i]
            invpp[i] = self.binExp(pp[i], primeFactors[i] - 2, primeFactors[i])

        # print("pp " + str(pp))
        # print("invpp " + str(invpp))

        for i in range(numFactors):
            nBasepp = self.baseConversion(n, primeFactors[i])
            rBasepp = self.baseConversion(r, primeFactors[i])
            rem = 1
            while len(rBasepp) < len(nBasepp):
                rBasepp.append(0)
            # print("rBasepp: " + str(rBasepp))
            # print("nBasepp: " + str(nBasepp))
            for j in range(len(rBasepp)):
                ncr = self.findNcR(nBasepp[j], rBasepp[j], factorial, primeFactors[i])
                # print(ncr)
                rem = (rem * ncr) % primeFactors[i]
                # print(rem)
            # print("rem " + str(rem))
            ans = (ans + ((rem * pp[i]) % mod) * invpp[i]) % mod

        return ans

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, r, m = input().split()
        n = int(n)
        r = int(r)
        m = int(m)
        obj = Solution()
        ans = obj.nCrModM(n, r, m)
        print(ans)


# } Driver Code Ends
