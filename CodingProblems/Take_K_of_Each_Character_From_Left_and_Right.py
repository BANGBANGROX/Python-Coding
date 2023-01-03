class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0 for _ in range(3)]
        i = n - 1
        j = n - 1
        ans = n

        for ch in s:
            count[ord(ch) - 97] += 1

        if count[0] < k or count[1] < k or count[2] < k:
            return -1

        while i >= 0:
            count[ord(s[i]) - 97] -= 1
            while count[0] < k or count[1] < k or count[2] < k:
                count[ord(s[j]) - 97] += 1
                j -= 1
            ans = min(ans, i + n - 1 - j)
            i -= 1

        return ans


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        k = int(input())

        solution = Solution()
        print(solution.takeCharacters(s, k))
