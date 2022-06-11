# User function Template for python3

class Solution:
    def nullPoints(self, n, a, getAnswer):
        # Your code goes here
        for i in range(n - 1):
            l = a[i]
            r = a[i + 1]
            while round(l, 2) != round(r, 2):
                mid = (l + r) / 2
                force = sum(1 / (x - mid) for x in a)
                if force == 0:
                    l = mid
                    break
                elif force < 0:
                    l = mid
                else:
                    r = mid
            getAnswer[i] = l


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        getAnswer = [0]*n
        ob = Solution()
        ob.nullPoints(n, a, getAnswer)

        for i in range(0, n-1):
            print("{:.2f}".format(getAnswer[i]), end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
