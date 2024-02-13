def compute_z_function(s: str) -> list:
    n = len(s)
    result = [0] * n
    left = 0
    right = 0

    for i in range(1, n):
        if i > right:
            left = right = i
            while right < n and s[right] == s[right - left]:
                right += 1
            result[i] = right - left
            right -= 1
        else:
            k = i - left
            if result[k] < right - i + 1:
                result[i] = result[k]
            else:
                left = i
                while right < n and s[right] == s[right - left]:
                    right += 1
                result[i] = right - left
                right -= 1

    return result


class Solution:

    @staticmethod
    def minimum_time_to_initial_state(word: str, k: int) -> int:
        z_function = compute_z_function(word)
        answer = 1
        n = len(word)

        while k * answer < n:
            if z_function[k * answer] >= n - k * answer:
                break
            answer += 1

        return answer


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        word = input()
        k = int(input())

        solution = Solution()
        print(solution.minimum_time_to_initial_state(word, k))
