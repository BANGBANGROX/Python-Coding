class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        n: int = len(arr)

        if n == 0:
            return []

        curr_rank: int = 1
        num_with_index: list[list[int]] = [[0] * 2 for _ in range(n)]
        answer: list[int] = [0] * n

        for i in range(n):
            num_with_index[i][0] = arr[i]
            num_with_index[i][1] = i

        num_with_index.sort()

        answer[num_with_index[0][1]] = 1
        last_num: int = num_with_index[0][0]

        for i in range(1, n):
            num: int = num_with_index[i][0]
            idx: int = num_with_index[i][1]
            if num > last_num:
                curr_rank += 1
            answer[idx] = curr_rank
            last_num = num

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        arr: list[int] = [0] * n
        for i in range(n):
            arr[i] = int(input())

        print(Solution().arrayRankTransform(arr=arr))
