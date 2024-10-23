# User function Template for python3


class Solution:
    def sameOccurrence(self, arr: list[int], x: int, y: int) -> int:
        # code here
        cnt_difference: int = 0
        count: dict[int, int] = {0: 1}
        answer: int = 0

        for num in arr:
            if num == x:
                cnt_difference += 1
            elif num == y:
                cnt_difference -= 1
            answer += count.get(cnt_difference, 0)
            count[cnt_difference] = count.get(cnt_difference, 0) + 1

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    tc: int = int(input())
    while tc > 0:
        arr: list[int] = list(map(int, input().strip().split()))
        x: int = int(input().strip())
        y: int = int(input().strip())
        ob: Solution = Solution()
        ans: int = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends
