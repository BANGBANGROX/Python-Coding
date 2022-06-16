# User function Template for python3

class Solution:
    def findSubString(self, s):
        # Your code goes here
        n = len(s)
        l = 0
        ans = int(1e9)
        count = {}
        required = 0
        done = 0

        for ch in s:
            if count.get(ch) == None:
                required += 1
                count[ch] = 0

        for r in range(n):
            count[s[r]] += 1
            if count[s[r]] == 1:
                done += 1
            if done == required:
                while count[s[l]] > 1:
                    count[s[l]] -= 1
                    l += 1
                ans = min(ans, r - l + 1)

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
