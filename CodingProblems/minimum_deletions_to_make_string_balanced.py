class Solution:
    def minimumDeletions(self, s: str) -> int:
        answer = 0
        b_cnt = 0

        for ch in s:
            if ch == "a":
                answer += 1
                answer = min(answer, b_cnt)
            else:
                b_cnt += 1

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(Solution().minimumDeletions(s=input()))
