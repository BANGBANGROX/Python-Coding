class MyCalendarTwo:
    def __init__(self):
        self.__intervals: list[list[int]] = []

    def book(self, start: int, end: int) -> bool:
        last_intersect: list[int] = None

        for curr_start, curr_end in self.__intervals:
            if start < curr_end and end > curr_start:
                if last_intersect is not None:
                    left: int = max(last_intersect[0], curr_start)
                    right: int = min(last_intersect[1], curr_end)
                    if left < right:
                        return False
                last_intersect = [curr_start, curr_end]

        self.__intervals.append([start, end])
        self.__intervals.sort()

        return True


if __name__ == "__main__":
    my_calendar_two: MyCalendarTwo = MyCalendarTwo()
    print(my_calendar_two.book(start=10, end=20))
    print(my_calendar_two.book(start=50, end=60))
    print(my_calendar_two.book(start=10, end=40))
    print(my_calendar_two.book(start=5, end=15))
