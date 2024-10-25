class Solution:
    def trappingWater(self, arr: list[int]) -> int:
        # code here
        left: int = 0
        right: int = len(arr) - 1
        max_left: int = arr[left]
        max_right: int = arr[right]
        answer: int = 0

        while left < right:
            max_left = max(max_left, arr[left])
            max_right = max(max_right, arr[right])
            if max_left < max_right:
                answer += max_left - arr[left]
                left += 1
            else:
                answer += max_right - arr[right]
                right -= 1

        return answer


# {
# Driver Code Starts
# Initial template for Python 3


def main():
    t: int = int(input())
    while t > 0:
        arr: list[int] = [int(x) for x in input().strip().split()]
        obj: Solution = Solution()
        print(obj.trappingWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
