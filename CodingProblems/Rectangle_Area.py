class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:

        aArea = (ay2 - ay1) * (ax2 - ax1)
        bArea = (by2 - by1) * (bx2 - bx1)
        xOverlap = min(ax2, bx2) - max(ax1, bx1)
        yOverlap = min(ay2, by2) - max(ay1, by1)
        ans = aArea + bArea

        if xOverlap > 0 and yOverlap > 0:
            ans -= xOverlap * yOverlap

        return ans


if __name__ == '__main__':
    solution = Solution()
    ax1 = int(input())
    ay1 = int(input())
    ax2 = int(input())
    ay2 = int(input())
    bx1 = int(input())
    by1 = int(input())
    bx2 = int(input())
    by2 = int(input())

    print(solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx1, by2))
