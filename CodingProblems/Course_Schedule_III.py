from typing import List
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        time = 0

        courses.sort(key=lambda x: x[1])

        for course in courses:
            if course[0] + time < course[1]:
                time += course[0]
                heapq.heappush(pq, -1 * course[0])
            elif len(pq) > 0 and -1 * pq[0] > course[0]:
                time += (course[0] + heapq.heappop(pq))
                heapq.heappush(pq, -1*course[0])

        return len(pq)
