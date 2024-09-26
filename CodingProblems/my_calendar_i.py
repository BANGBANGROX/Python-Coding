class MyCalendar:

    def __init__(self):
        self.__intervals: list[list[int]] = []

    def book(self, start: int, end: int) -> bool:
        for interval in self.__intervals:
            if start < interval[1] and end > interval[0]:
                return False

        self.__intervals.append([start, end])
        self.__intervals.sort()

        return True


if __name__ == "__main__":
    my_calendar = MyCalendar()
    print(my_calendar.book(start=10, end=20))
    print(my_calendar.book(start=15, end=25))
    print(my_calendar.book(start=20, end=30))
