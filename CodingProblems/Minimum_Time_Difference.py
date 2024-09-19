TOTAL_TIME = 24 * 60


class Solution:
    def findMinDifference(self, time_points: list[str]) -> int:
        visited: list[bool] = [False] * TOTAL_TIME
        first_time: int = TOTAL_TIME
        last_time: int = 0
        previous_time: int = 0
        answer: int = TOTAL_TIME

        for time_point in time_points:
            time_point_list: list[str] = time_point.split(":")
            hours: int = int(time_point_list[0])
            minutes: int = int(time_point_list[1])
            final_time = hours * 60 + minutes
            if visited[final_time]:
                return 0
            visited[final_time] = True

        for current_time in range(TOTAL_TIME):
            if visited[current_time]:
                if first_time != TOTAL_TIME:
                    answer = min(answer, current_time - previous_time)
                first_time = min(first_time, current_time)
                last_time = max(last_time, current_time)
                previous_time = current_time

        answer = min(answer, TOTAL_TIME - last_time + first_time)

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        time_points: list[str] = [None] * n
        for i in range(n):
            time_points[i] = input()

        print(Solution().findMinDifference(time_points=time_points))
