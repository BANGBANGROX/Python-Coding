# User function Template for python3


def Search(arr: list[int], n: int, k: int) -> int:
    # code here
    left: int = 0
    right: int = n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        if arr[left] <= arr[mid]:
            if k >= arr[left] and k <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if k <= arr[right] and k >= arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    tcs: int = int(input())
    for _ in range(tcs):
        n: int = int(input())
        arr: list[int] = [int(x) for x in input().split()]
        k: int = int(input())

        print(Search(arr, n, k))

        print("~")
# } Driver Code Ends
