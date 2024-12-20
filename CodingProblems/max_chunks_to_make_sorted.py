class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        answer: int = 0
        n: int = len(arr)
        max_value: int = 0

        for i in range(n):
            max_value = max(max_value, arr[i])
            if max_value == i:
                answer += 1

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        arr: list[int] = [int(input()) for _ in range(n)]

        print(Solution().maxChunksToSorted(arr=arr))