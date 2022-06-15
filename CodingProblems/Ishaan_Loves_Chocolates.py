# User function Template for python3

def chocolates(arr, n):
    # Complete the function
    l = 0
    r = n - 1

    while l < r:
        if arr[l] < arr[r]:
            r -= 1
        else:
            l += 1

    return arr[l]


# {
#  Driver Code Starts
# Initial Template for Python 3

for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = chocolates(arr, n)
    print(ans)


# } Driver Code Ends
