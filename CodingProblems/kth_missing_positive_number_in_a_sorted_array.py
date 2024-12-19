#User function Template for python3
class Solution:
    def kthMissing(self, arr: list[int], k: int) -> int:
        # code here
        left: int = 0
        right: int = len(arr) - 1

        while left <= right:
            mid = (left + ((right - left) >> 1))
            missing_cnt = arr[mid] - mid - 1
            if missing_cnt < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k


#{
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t: int = int(input())
    while t:
        t -= 1
        A: list[int] = [int(x) for x in input().strip().split()]
        nd: list[int] = [int(x) for x in input().strip().split()]
        D: int = nd[0]
        ob: Solution = Solution()
        ans: int = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends