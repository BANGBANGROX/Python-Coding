#User function Template for python3

class Solution:
    def maximizeSum(self, nums: list[int], n: int, k: int) -> int:
        # Your code goes here
        least_abs_value: int = 10**18
        answer: int = 0
        cnt: int = 0

        for num in nums:
            least_abs_value = min(least_abs_value, abs(num))
            if num < 0:
                if cnt < k:
                    cnt += 1
                    num *= -1
            answer += num

        k -= cnt
        k %= 2

        if k > 0:
            answer -= 2 * least_abs_value

        return answer

#{
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T: int = int(input())

    while T > 0:
        sz: list[int] = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a: list[int] = [int(x) for x in input().strip().split()]
        ob: Solution =Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


        print("~")
if __name__ == "__main__":
    main()



# } Driver Code Ends