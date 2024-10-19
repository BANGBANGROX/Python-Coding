class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1 or k == 1:
            return "0"

        length: int = (1 << n) - 1
        mid: int = length // 2

        if mid == k - 1:
            return "1"

        if k - 1 < mid:
            return self.findKthBit(n=n - 1, k=k)

        return "0" if self.findKthBit(n=n - 1, k=length - k + 1) == "1" else "1"


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().findKthBit(n=int(input()), k=int(input())))
