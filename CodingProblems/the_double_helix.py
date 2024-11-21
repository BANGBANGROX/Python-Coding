class Solution:
    def find_max_sum(self, first: list[int], second: list[int]) -> int:
        m: int = len(first)
        n: int = len(second)
        i: int = 0
        j: int = 0
        first_sum: int = 0
        second_sum: int = 0
        answer: int = 0

        while i < m or j < n:
            if i == m:
                while j < n:
                    second_sum += second[j]
                    j += 1
            elif j == n:
                while i < m:
                    first_sum += first[i]
                    i += 1
            elif first[i] < second[j]:
                first_sum += first[i]
                i += 1
            elif second[j] < first[i]:
                second_sum += second[j]
                j += 1
            else:
                answer += max(first_sum, second_sum)
                first_sum = second_sum = first[i]
                i += 1
                j += 1

        answer += max(first_sum, second_sum)

        return answer


if __name__ == "__main__":
    while True:
        first: list[int] = input().split(" ")
        if first[0] == "0":
            break
        second: list[int] = input().split(" ")
        first = [int(x) for x in first]
        second = [int(x) for x in second]

        print(Solution().find_max_sum(first=first[1:], second=second[1:]))
