import math


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int,
                    uniqueCnt1: int, uniqueCnt2: int) -> int:
        l = 1
        r = 1e10
        ans = -1
        lcm = math.lcm(divisor1, divisor2)

        while l <= r:
            mid = (l + r) // 2
            cnt1 = mid - mid // divisor1
            cnt2 = mid - mid // divisor2
            combined = mid - mid // lcm
            if cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and combined >= uniqueCnt1 + uniqueCnt2:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        divisor1 = int(input())
        divisor2 = int(input())
        uniqueCnt1 = int(input())
        uniqueCnt2 = int(input())

        solution = Solution()
        print(solution.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2))
