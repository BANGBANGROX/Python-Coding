# User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self, s: str) -> int:
        # code here
        open_cnt: int = 0
        close_cnt: int = 0
        imbalance: int = 0
        answer: int = 0

        for ch in s:
            if ch == "[":
                open_cnt += 1
                if imbalance > 0:
                    answer += imbalance
            else:
                close_cnt += 1
            imbalance = close_cnt - open_cnt

        return answer


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t: int = int(input())
    for _ in range(t):

        S: int = str(input())
        ob: Solution = Solution()
        print(ob.minimumNumberOfSwaps(S))
        print("~")
# } Driver Code Ends
