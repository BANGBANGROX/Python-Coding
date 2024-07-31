class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        answer = 0
        one_cnt = 0

        for ch in s:
            if ch == "0":
                answer += 1
                answer = min(answer, one_cnt)
            else:
                one_cnt += 1

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(Solution().minFlipsMonoIncr(s=input()))
