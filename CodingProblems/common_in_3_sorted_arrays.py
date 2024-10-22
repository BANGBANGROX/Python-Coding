# User function Template for python3


class Solution:
    def __common_elements_handler(
        self, nums1: list[int], nums2: list[int]
    ) -> list[int]:
        m: int = len(nums1)
        n: int = len(nums2)
        i: int = 0
        j: int = 0
        result: list[int] = []

        while i < m and j < n:
            while i < m - 1 and nums1[i] == nums1[i + 1]:
                i += 1
            while j < n - 1 and nums2[j] == nums2[j + 1]:
                j += 1
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

    def commonElements(
        self, arr1: list[int], arr2: list[int], arr3: list[int]
    ) -> list[int]:
        # Code Here
        return self.__common_elements_handler(
            arr1, self.__common_elements_handler(arr2, arr3)
        )


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))

# } Driver Code Ends
