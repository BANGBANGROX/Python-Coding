import heapq


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        pq: list[list[int]] = []
        k: int = len(nums)
        INF: int = 10**9
        max_val: int = -1 * INF
        range_start: int = 0
        range_end: int = INF

        for i in range(k):
            current_val: int = nums[i][0]
            max_val: int = max(max_val, current_val)
            pq.append([current_val, i, 0])

        heapq.heapify(pq)

        while len(pq) == k:
            data: list[int] = heapq.heappop(pq)
            min_val: int = data[0]
            row: int = data[1]
            col: int = data[2]

            if max_val - min_val < range_end - range_start:
                range_start = min_val
                range_end = max_val

            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                max_val = max(max_val, next_val)
                heapq.heappush(pq, [next_val, row, col + 1])

        return [range_start, range_end]


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        k: int = int(input())
        nums: list[list[int]] = []
        for i in range(k):
            size: int = int(input())
            curr_list: list[int] = []

            for j in range(size):
                curr_list.append(int(input()))

            nums.append(curr_list)

        print(Solution().smallestRange(nums=nums))
