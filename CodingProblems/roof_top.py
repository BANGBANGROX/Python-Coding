#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr: list[int]):
        #Your code here
        answer: int = 0
        current: int = 0
        n: int = len(arr)
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                current += 1
            else:
                answer = max(answer, current)
                current = 0
        
        answer = max(answer, current)
        
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends