class Solution:
    def __init__(self) -> None:
        self.__factory_positions: list[int] = None
        self.__robot_positions: list[int] = None
        self.__dp: list[list[int]] = None
        self.__factor_cnt: int = 0
        self.__robot_cnt: int = 0

    def __minimum_total_distance_handler(self, robot_idx: int, factory_idx: int) -> int:
        if robot_idx == self.__robot_cnt:
            return 0

        if factory_idx == self.__factor_cnt:
            return 10**12

        if self.__dp[robot_idx][factory_idx] != -1:
            return self.__dp[robot_idx][factory_idx]

        take: int = abs(
            self.__factory_positions[factory_idx] - self.__robot_positions[robot_idx]
        ) + self.__minimum_total_distance_handler(
            robot_idx=robot_idx + 1, factory_idx=factory_idx + 1
        )
        skip: int = self.__minimum_total_distance_handler(
            robot_idx=robot_idx, factory_idx=factory_idx + 1
        )

        self.__dp[robot_idx][factory_idx] = min(take, skip)

        return self.__dp[robot_idx][factory_idx]

    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        self.__robot_positions = robot
        self.__robot_cnt = len(robot)
        self.__factory_positions = []

        for curr_factory in factory:
            for _ in range(curr_factory[1]):
                self.__factory_positions.append(curr_factory[0])

        self.__robot_positions.sort()
        self.__factory_positions.sort()

        self.__factor_cnt = len(self.__factory_positions)
        self.__dp = [
            [-1 for _ in range(self.__factor_cnt)] for _ in range(self.__robot_cnt)
        ]

        return self.__minimum_total_distance_handler(robot_idx=0, factory_idx=0)


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        robot_cnt: int = int(input())
        robot: list[int] = [0] * robot_cnt
        for i in range(robot_cnt):
            robot[i] = int(input())
        factory_cnt: int = int(input())
        factory: list[list[int]] = [[0, 0] for _ in range(factory_cnt)]
        for i in range(factory_cnt):
            factory[i][0] = int(input())
            factory[i][1] = int(input())

        print(Solution().minimumTotalDistance(robot=robot, factory=factory))
