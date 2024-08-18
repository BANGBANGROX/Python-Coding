from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        cnt = 0

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                cnt = cnt + 1 if cnt > 0 else 1
            elif arr[i] < arr[i + 1]:
                cnt = cnt - 1 if cnt < 0 else -1
            else:
                cnt = 0
            answer = max(answer, abs(cnt))
            cnt *= -1

        return answer + 1


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        arr = List()

        for _ in range(n):
            arr.append(int(input()))

        print(Solution().maxTurbulenceSize(arr=arr))
