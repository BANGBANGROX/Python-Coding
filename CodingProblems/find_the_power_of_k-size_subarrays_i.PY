class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        answer: list[int] = []
        n: int = len(nums)
        left: int = 0
        right: int = k - 1

        while right < n:
            flag: bool = True
            for i in range(left + 1, right + 1):
                if nums[i] != nums[i - 1] + 1:
                    flag = False
                    break
            if flag:
                answer.append(nums[right])
            else:
                answer.append(-1)
            left += 1
            right += 1

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums[i] = int(input())
        k = int(input())

        print(Solution().resultsArray(nums=nums, k=k))
