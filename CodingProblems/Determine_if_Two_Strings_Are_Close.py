class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = [0 for _ in range(26)]
        count2 = [0 for _ in range(26)]
        present1 = [False for _ in range(26)]
        present2 = [False for _ in range(26)]

        for ch in word1:
            count1[ord(ch) - 97] += 1
            present1[ord(ch) - 97] = True

        for ch in word2:
            count2[ord(ch) - 97] += 1
            present2[ord(ch) - 97] = True

        count1.sort()
        count2.sort()

        for i in range(26):
            if count1[i] != count2[i] or present1[i] != present2[i]:
                return False

        return True


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        word1 = input()
        word2 = input()

        solution = Solution()
        print(solution.closeStrings(word1, word2))
