# User function Template for python3

class Solution:
    def profession(self, level, pos):
        # code here
        if pos == 1:
            return 'e'

        newPos = (pos + 1) // 2

        ch = self.profession(level - 1, newPos)

        if 2 * newPos - 1 == pos:
            return ch

        if ch == 'e':
            return 'd'

        return 'e'

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        level, pos = [int(x) for x in input().split()]

        ob = Solution()
        if(ob.profession(level, pos) == 'd'):
            print("Doctor")
        else:
            print("Engineer")
# } Driver Code Ends
