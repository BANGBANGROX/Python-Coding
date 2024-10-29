# User function Template for python3


class Solution:
    def __max_area_rectangle_in_array(self, nums: list[int], n: int) -> int:
        stack: list[int] = []
        max_area: int = 0

        for i in range(n):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                previous_smaller = stack[-1] if len(stack) > 0 else -1
                max_area = max(max_area, nums[idx] * (i - previous_smaller - 1))
            stack.append(i)

        while len(stack) > 0:
            idx = stack.pop()
            previous_smaller = stack[-1] if len(stack) > 0 else -1
            max_area = max(max_area, nums[idx] * (n - previous_smaller - 1))

        return max_area

    def maxArea(self, matrix: list[list[int]], m: int, n: int) -> int:
        # code here
        answer: int = self.__max_area_rectangle_in_array(matrix[0], n)

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] > 0:
                    matrix[i][j] += matrix[i - 1][j]
            answer = max(answer, self.__max_area_rectangle_in_array(matrix[i], n))

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3


# Driver Code
if __name__ == "__main__":
    t: int = int(input())

    for _ in range(t):
        R, C = map(int, input().strip().split())
        A: list[int] = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)

        print(Solution().maxArea(A, R, C))
        print("~")

# } Driver Code Ends
