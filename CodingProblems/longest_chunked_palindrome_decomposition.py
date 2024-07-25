class Solution:
    def longestDecomposition(self, text: str) -> int:
        answer = 0
        left = ""
        right = ""
        n = len(text)
        
        for i in range(n):
            left += text[i]
            right = text[n - i - 1] + right
            if left == right:
                answer += 1
                left = ""
                right = ""
        
        return answer


if __name__ == "__main__":
    test_cases = int(input())
    
    for _ in range(test_cases):
        print(Solution().longestDecomposition(input()))