class Solution:
    def __check_count(self, count1: list[int], count2: list[int]) -> bool:
        for cnt1, cnt2 in zip(count1, count2):
            if cnt1 != cnt2:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        m: int = len(s1)
        n: int = len(s2)

        if m > n:
            return False

        left: int = 0
        right: int = m - 1
        count1: list[int] = [0] * 26
        count2: list[int] = [0] * 26

        for i in range(m):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1

        while right < n:
            if self.__check_count(count1=count1, count2=count2):
                return True
            count2[ord(s2[left]) - ord("a")] -= 1
            left += 1
            right += 1
            if right < n:
                count2[ord(s2[right]) - ord("a")] += 1

        return False


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().checkInclusion(s1=input(), s2=input()))
