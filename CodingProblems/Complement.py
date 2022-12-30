# User function Template for python3
class Solution:
    def findRange(self, s, n):
        # code here
        start = -1
        end = -1
        l = 0
        currentCount = 0
        maxCount = 0

        for i in range(0, n):
            if s[i] == "0":
                currentCount += 1
            else:
                currentCount -= 1
            if currentCount < 0:
                l = i + 1
                currentCount = 0
            elif currentCount > maxCount:
                maxCount = currentCount
                start = l
                end = i

        if end == -1:
            return [-1]

        return [start + 1, end + 1]

        # {
     # Driver Code Starts
if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        s = input()
        ob = Solution()
        ans = ob.findRange(s, n)
        if len(ans) == 1:
            print(ans[0])
        else:
            print(str(ans[0])+" "+str(ans[1]))
        tc = tc-1
# } Driver Code Ends
