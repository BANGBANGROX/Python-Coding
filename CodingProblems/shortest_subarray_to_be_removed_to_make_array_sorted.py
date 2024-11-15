class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n: int = len(arr)
        left: int = 0
        right: int = n - 1

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        answer: int = right

        while left < right:
            while right < n and arr[right] < arr[left]:
                right += 1
            answer = min(answer, right - left - 1)
            left += 1
            if arr[left] < arr[left - 1]:
                break

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        arr: list[int] = []
        for i in range(n):
            arr[i] = int(input())

        print(Solution().findLengthOfShortestSubarray(arr=arr))
