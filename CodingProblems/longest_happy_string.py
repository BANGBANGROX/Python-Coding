import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq: list[list[int | str]] = []
        answer: list[str] = []

        if a > 0:
            pq.append([-1 * a, "a"])

        if b > 0:
            pq.append([-1 * b, "b"])

        if c > 0:
            pq.append([-1 * c, "c"])

        heapq.heapify(pq)

        while len(pq) > 1:
            first: list[str | any] = heapq.heappop(pq)
            second: list[str | any] = heapq.heappop(pq)
            first_cnt: int = -1 * first[0]
            first_char: str = first[1]
            second_cnt: int = -1 * second[0]
            second_char: str = second[1]

            if first_cnt > 1:
                answer.append(first_char)
                answer.append(first_char)
                first_cnt -= 2
            else:
                answer.append(first_char)
                first_cnt -= 1

            if second_cnt > 1 and second_cnt >= first_cnt:
                answer.append(second_char)
                answer.append(second_char)
                second_cnt -= 2
            else:
                answer.append(second_char)
                second_cnt -= 1

            if first_cnt > 0:
                heapq.heappush(pq, [-1 * first_cnt, first_char])

            if second_cnt > 0:
                heapq.heappush(pq, [-1 * second_cnt, second_char])

        if len(pq) > 0:
            if -1 * pq[0][0] > 1:
                answer.append(pq[0][1])
                answer.append(pq[0][1])
            else:
                answer.append(pq[0][1])

        return "".join(answer)


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(
            Solution().longestDiverseString(
                a=int(input()), b=int(input()), c=int(input())
            )
        )
