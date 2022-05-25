# User function Template for python3

class Solution:
    def reArrange(self, arr, n):
        # code here
        i = 0
        j = 1

        while i < n and j < n:
            if arr[i] % 2 == 0:
                i += 2
            elif arr[j] % 2 == 1:
                j += 2
            else:
                arr[j] = arr[i] + arr[j]
                arr[i] = arr[j] - arr[i]
                arr[j] = arr[j] - arr[i]
                i += 2
                j += 2

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


def check(arr, n):
    flag = 1
    c = d = 0
    for i in range(n):
        if i % 2 == 0:
            if arr[i] % 2:
                flag = 0
                break
            else:
                c += 1
        else:
            if arr[i] % 2 == 0:
                flag = 0
                break
            else:
                d += 1
    if c != d:
        flag = 0

    return flag


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ob.reArrange(arr, N)

        print(check(arr, N))

# } Driver Code Ends
