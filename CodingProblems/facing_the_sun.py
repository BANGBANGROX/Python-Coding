# User function Template for python3


class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height: list[int]) -> int:
        # code here
        answer: int = 1
        running_max: int = height[0]
        n: int = len(height)

        for i in range(1, n):
            if height[i] > running_max:
                answer += 1
                running_max = height[i]

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends
