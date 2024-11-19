# User function Template for python3


class Solution:
    def findMin(self, arr: list[int]) -> int:
        # complete the function here
        left: int = 0
        right: int = len(arr) - 1
        answer: int = 10**9

        while left <= right:
            mid: int = left + ((right - left) >> 1)
            if arr[left] <= arr[mid]:
                answer = min(answer, arr[left])
                left = mid + 1
            elif arr[mid] <= arr[right]:
                answer = min(answer, arr[mid])
                right = mid - 1
            else:
                return arr[mid]

        return answer


# {
# Driver Code Starts
def main():
    T: int = int(input())

    while T > 0:
        a: list[int] = list(
            map(int, input().strip().split())
        )  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
