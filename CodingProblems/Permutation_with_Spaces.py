#User function Template for python3

class Solution:
    def permutation (self, s):
        # code here
        ans = [];
        currentString = "";

        def permutationUtil(self, s, i : int, currentString) :
            if i == len(s) :
                ans.append(currentString);
                return;

            # Take the current character
            permutationUtil(s, i + 1, currentString + s[i]);

            # If the previous character wasn't space take space
            if len(currentString) > 0 and currentString[len(currentString) - 1] != ' ' :
                permutationUtil(s, i, currentString + ' ');     
                
        permutationUtil(s, 0, currentString);
        ans.sort();

        return ans;

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends