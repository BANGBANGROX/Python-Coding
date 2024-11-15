class Solution:

    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr: list[int]) -> int:
        # Code here
        n: int = len(arr)
        num_and_indexes: list[list[int]] = []
        visited: list[bool] = [False] * n
        answer: int = 0

        for i in range(n):
            num_and_indexes.append([arr[i], i])

        num_and_indexes.sort()

        for i in range(n):
            if visited[i] or num_and_indexes[i][1] == i:
                continue
            j: int = i
            cycle_size: int = 0
            while not visited[j]:
                visited[j] = True
                j = num_and_indexes[j][1]
                cycle_size += 1
            answer += cycle_size - 1

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t: int = int(input())
    while t > 0:
        arr: list[int] = list(map(int, input().split()))
        ob: Solution = Solution()
        res: int = ob.minSwaps(arr)
        print(res)
        t -= 1
# } Driver Code Ends
