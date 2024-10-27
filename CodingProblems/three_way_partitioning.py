# User function template for Python


class Solution:
    # Function to partition the array around the range such
    # that array is divided into three parts.
    def threeWayPartition(self, nums: list[int], a: int, b: int) -> None:
        n: int = len(array)
        i: int = 0
        j: int = n - 1
        itr: int = 0

        while itr < n and j >= itr:
            if nums[itr] < a:
                nums[itr], nums[i] = nums[i], nums[itr]
                itr += 1
                i += 1
            elif nums[itr] > b:
                nums[itr], nums[j] = nums[j], nums[itr]
                j -= 1
            else:
                itr += 1


# {
# Driver Code Starts
# Initial template for Python

from collections import Counter
from collections.abc import Sequence

if __name__ == "__main__":
    t: int = int(input())
    for i in range(t):
        n: int = int(input())
        array: list[int] = list(map(int, input().strip().split()))
        original: Counter = Counter(array)
        a, b = list(map(int, input().strip().split()))
        ob: Solution = Solution()
        ob.threeWayPartition(array, a, b)

        if not isinstance(array, Sequence) or isinstance(array, str):
            print(0)
        else:
            k1 = k2 = k3 = 0
            for e in array:
                if e > a:
                    k3 += 1
                elif e <= a and e >= b:
                    k2 += 1
                elif e < a:
                    k1 += 1

            m1 = m2 = m3 = 0
            for e in range(k1):
                if array[e] < a:
                    m1 += 1
            for e in range(k1, k1 + k2):
                if array[e] <= a and array[e] >= b:
                    m2 += 1
            for e in range(k1 + k2, k1 + k2 + k3):
                if array[e] >= a:
                    m3 += 1

            flag = False
            if k1 == m1 and k2 == m2 and k3 == m3:
                flag = True
            for e in range(len(array)):
                original[array[e]] -= 1
            for e in range(len(array)):
                if original[array[e]] != 0:
                    flag = False
            if flag:
                print(1)
            else:
                print(0)

        print("~")
# } Driver Code Ends
