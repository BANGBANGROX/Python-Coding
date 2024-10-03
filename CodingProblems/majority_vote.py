class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums: list[int]) -> list[int]:
        # Your Code goes here.
        n: int = len(nums)
        req_cnt: int = n // 3
        first_element: int = -1
        second_element: int = -1
        first_cnt: int = 0
        second_cnt: int = 0

        for num in nums:
            if first_cnt == 0 and second_element != num:
                first_cnt += 1
                first_element = num
            elif second_cnt == 0 and first_element != num:
                second_cnt += 1
                second_element = num
            elif num == first_element:
                first_cnt += 1
            elif num == second_element:
                second_cnt += 1
            else:
                first_cnt -= 1
                second_cnt -= 1

        first_cnt = second_cnt = 0

        for num in nums:
            if num == first_element:
                first_cnt += 1
            elif num == second_element:
                second_cnt += 1

        if first_cnt > req_cnt and second_cnt > req_cnt:
            return [first_element, second_element]

        if first_cnt > req_cnt:
            return [first_element]

        if second_cnt > req_cnt:
            return [second_element]

        return [-1]


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
