# User function Template for python3
class Solution:
    def count_groups(self, arr: list[int]) -> int:
        total_xor: int = 0
        MOD: int = 10**9 + 7

        for num in arr:
            total_xor ^= num

        if total_xor != 0:
            return 0

        return (pow(base=2, exp=len(arr) - 1, mod=MOD) - 1 + MOD) % MOD


# {
# Driver Code Starts
if __name__ == "__main__":
    t: int = int(input())
    while t > 0:
        arr: list[int] = list(map(int, input().split()))
        ob: Solution = Solution()
        res: int = ob.count_groups(arr)
        print(res)
        t -= 1

# } Driver Code Ends
