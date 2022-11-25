# User function Template for python3

class Solution:
    def binarySearch(self, nums, key):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if nums[mid] == key:
                return True
            elif nums[mid] > key:
                r = mid - 1
            else:
                l = mid + 1

        return False

    def lowerBound(self, nums, key):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if nums[mid] >= key:
                r = mid - 1
            else:
                l = mid + 1

        return l

    def minInsAndDel(self, nums1, nums2, m, n):
        # code here
        lis = []

        for num in nums1:
            if self.binarySearch(nums2, num):
                idx = self.lowerBound(lis, num)
                if idx >= len(lis):
                    lis.append(num)
                else:
                    lis[idx] = num

        return m + n - 2 * len(lis)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        ob = Solution()
        print(ob.minInsAndDel(A, B, N, M))
# } Driver Code Ends
