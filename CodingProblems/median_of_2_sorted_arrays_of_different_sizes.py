# User function Template for python3


class Solution:
    def MedianOfArrays(self, nums1, nums2):
        # code here
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.MedianOfArrays(nums1=nums2, nums2=nums1)

        total_size = m + n
        left = 0
        right = m
        INF = 10**9

        while left <= right:
            cut1 = left + ((right - left) >> 1)
            cut2 = (total_size + 1) // 2 - cut1
            first1, first2, last1, last2 = -1 * INF, -1 * INF, INF, INF
            if cut1 > 0:
                first1 = nums1[cut1 - 1]
            if cut2 > 0:
                first2 = nums2[cut2 - 1]
            if cut1 < m:
                last1 = nums1[cut1]
            if cut2 < n:
                last2 = nums2[cut2]
            if first1 <= last2 and first2 <= last1:
                if (total_size & 1) > 0:
                    return max(first1, first2)
                first = max(first1, first2)
                last = min(last1, last2)
                if ((first + last) & 1) > 0:
                    return (first + last) / 2
                return (first + last) // 2
            if first1 > last2:
                right = cut1 - 1
            else:
                left = cut1 + 1

        return -1


# {
# Driver Code Starts
if __name__ == "__main__":
    tcs = int(input())

    for _ in range(tcs):
        m = input()
        arr1 = [int(x) for x in input().split()]
        n = input()
        arr2 = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.MedianOfArrays(arr1, arr2))

# } Driver Code Ends
