from math import log2


def compute_n_c_r(n: int, r: int) -> int:
    result = 1

    for i in range(1, r + 1):
        result *= (n - r + i)
        result //= i

    return result


class Solution:
    def __init__(self):
        self.k = None
        self.n = None

    def compute_nums_with_at_most_k_set_bits(self, num: int, bits: int) -> int:
        if bits == 0:
            return 1

        if num == 0:
            return 0

        last_bit = int(log2(num))

        if last_bit < bits - 1:
            return 0

        return compute_n_c_r(last_bit, bits) + \
            self.compute_nums_with_at_most_k_set_bits(num ^ (1 << last_bit), bits - 1)

    def check(self, num: int) -> bool:
        result = 0

        for i in range(self.k + 1):
            result += self.compute_nums_with_at_most_k_set_bits(num, i)
            if result >= self.n:
                return True

        return False

    def findNthNumber(self, n: int, k: int) -> int:
        self.n = n
        self.k = k
        low = 0
        high = 10 ** 15

        while low < high:
            mid = (low + ((high - low) >> 1))
            if self.check(mid):
                high = mid
            else:
                low = mid + 1

        return low


# code here


# {
# Driver Code Starts


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())

        obj = Solution()
        res = obj.findNthNumber(n, k)

        print(res)

# } Driver Code Ends
