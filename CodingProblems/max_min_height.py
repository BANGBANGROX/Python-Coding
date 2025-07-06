class Solution:
    def __init__(self):
        self.__arr: list[int] = []
        self.__k: int = 0
        self.__w: int = 0
        self.__n: int = 0

    def max_min_height(self, arr: list[int], k: int, w: int) -> int:
        self.__arr = arr
        self.__k = k
        self.__w = w
        self.__n = len(arr)
        min_height: int = min(arr)
        left: int = min_height
        right: int = min_height + k
        answer: int = -1

        while left <= right:
            mid = (left + ((right - left) >> 1))
            if self.__check(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer

    def __check(self, target_height: int) -> bool:
        dp: list[int] = [0] * (self.__n + 1)
        net_increase: int = 0
        days_taken: int = 0

        for (i, height) in enumerate(self.__arr):
            net_increase += dp[i]
            final_height: int = height + net_increase
            if final_height < target_height:
                gap: int = target_height - final_height
                if days_taken + gap > self.__k:
                    return False
                net_increase += gap
                days_taken += gap
                dp[i] += gap
                dp[min(i + self.__w, self.__n)] -= gap

        return True



# code here


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        arr: list[int] = [int(input()) for _ in range(n)]
        k: int = int(input())
        w: int = int(input())

        print(Solution().max_min_height(arr, k, w))
