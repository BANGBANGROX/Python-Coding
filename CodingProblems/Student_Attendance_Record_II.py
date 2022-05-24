class Solution:
    def checkRecord(self, n: int) -> int:
        a1 = 1  # 00
        a2 = 1  # 01
        a3 = 0  # 02
        a4 = 1  # 10
        a5 = 0  # 11
        a6 = 0  # 12
        mod = int(1e9 + 7)

        for i in range(n):
            newA1 = (a1 + a2 + a3) % mod
            newA2 = a1
            newA3 = a2
            newA4 = (a1 + a2 + a3 + a4 + a5 + a6) % mod
            newA5 = a4
            newA6 = a5
            a1 = newA1
            a2 = newA2
            a3 = newA3
            a4 = newA4
            a5 = newA5
            a6 = newA6

        return (a1 + a2 + a3 + a4 + a5 + a6) % mod
