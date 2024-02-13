class Solution:
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.d = None
        self.c = None

    def check(self, num: int) -> bool:
        while num > 0:
            dig = num % 10
            if dig != self.c and dig != self.d:
                return False
            num //= 10

        return True

    def computeInverse(self, num: int) -> int:
        power = self.MOD - 2
        result = 1

        while power > 0:
            if power & 2 > 0:
                result = (result * num) % self.MOD
                power -= 1
            num = (num * num) % self.MOD
            power >>= 1

        return result

    def bestNumbers(self, n: int, a: int, b: int, c: int, d: int) -> int:
        self.c = c
        self.d = d
        factorial = [0 for _ in range(n + 1)]
        inverse_factorial = [0 for _ in range(n + 1)]
        answer = 0

        factorial[0] = inverse_factorial[0] = 1

        for i in range(1, n + 1):
            factorial[i] = (factorial[i - 1] * i) % self.MOD
            inverse_factorial[i] = self.computeInverse(factorial[i])

        for i in range(0, n + 1):
            num = i * a + (n - i) * b
            if self.check(num):
                nci = (((factorial[n] * inverse_factorial[n - i]) % self.MOD) *
                       inverse_factorial[i]) % self.MOD
                answer = (answer + nci) % self.MOD

        return answer


# code here


# { 
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        A = int(input())

        B = int(input())

        C = int(input())

        D = int(input())

        obj = Solution()
        res = obj.bestNumbers(N, A, B, C, D)

        print(res)

# } Driver Code Ends
