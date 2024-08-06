class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(Solution().nthPersonGetsNthSeat(n=int(input())))
