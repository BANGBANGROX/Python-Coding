class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        len1 = len(s1)
        len2 = len(s2)
        i = 0
        j = 0
        cnt1 = 0
        cnt2 = 0

        while cnt1 < n1:
            if s1[i] == s2[j]:
                j += 1
                if j == len2:
                    cnt2 += 1
                    j = 0
            i += 1
            if i == len1:
                cnt1 += 1
                i = 0

        return cnt2 / n2


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(
            Solution().getMaxRepetitions(
                s1=input(), n1=int(input()), s2=input(), n2=int(input())
            )
        )
