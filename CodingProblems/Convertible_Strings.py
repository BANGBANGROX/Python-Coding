from typing import List

from typing import List


def calculate_gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return calculate_gcd(b, a % b)


class Solution:
    def CompatibleStrings(self, n: int, words1: List[str], words2: List[str]) -> List[int]:
        answer = list()

        for i in range(n):
            frequency_differences = []
            word1 = words1[i]
            word2 = words2[i]
            frequency_of_word1 = [0] * 26
            frequency_of_word2 = [0] * 26
            ptr1 = 0
            ptr2 = 0
            for ch in word1:
                frequency_of_word1[ord(ch) - ord('a')] += 1
            for ch in word2:
                frequency_of_word2[ord(ch) - ord('a')] += 1
            while ptr2 < 25:
                ptr1 += (frequency_of_word1[ptr2] - frequency_of_word2[ptr2])
                if ptr1 < 0:
                    break
                elif ptr1 > 0:
                    frequency_differences.append(ptr1)
                ptr2 += 1
            if ptr2 < 25 or (ptr1 + frequency_of_word1[ptr2] != frequency_of_word2[ptr2]):
                answer.append(0)
            else:
                if len(frequency_differences) == 0:
                    answer.append(1)
                else:
                    gcd = frequency_differences[0]
                    for j in range(1, len(frequency_differences)):
                        gcd = calculate_gcd(gcd, frequency_differences[j])
                    answer.append(0 if gcd == 1 else 1)

        return answer

# code here


# {
# Driver Code Starts

class StringArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = input().strip().split()  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        A1 = [el for el in input().split()]
        A2 = [el for el in input().split()]

        obj = Solution()
        res = obj.CompatibleStrings(N, A1, A2)

        IntArray().Print(res)

# } Driver Code Ends
