# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
class Solution:
    def smallestNumber(self, s: int, d: int) -> str:
        if s > 9 * d:
            return "-1"

        s -= 1
        number = ["0"] * d

        for i in range(d - 1, 0, -1):
            if s > 9:
                number[i] = "9"
                s -= 9
            else:
                number[i] = chr(ord("0") + s)
                s = 0

        number[0] = chr(ord("0") + s + 1)

        return "".join(number)



# code here


# {
# Driver Code Starts.
# Position this line where user code will be pasted.

import sys

input = sys.stdin.read
data = input().split()

t: int = int(data[0])
index: int = 1

for _ in range(t):
    s: int = int(data[index])
    d: int = int(data[index + 1])
    index += 2
    ob: Solution = Solution()
    print(ob.smallestNumber(s, d))
    print("~")
# } Driver Code Ends