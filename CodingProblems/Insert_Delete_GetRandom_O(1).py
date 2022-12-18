import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.index[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        lastValue = self.nums[-1]
        valIndex = self.index[val]

        if valIndex != len(self.nums) - 1:
            self.nums[valIndex] = lastValue
            self.index[lastValue] = valIndex

        self.index.pop(val)
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        ind = random.randint(0, len(self.nums) - 1)

        return self.nums[ind]


if __name__ == "__main__":
    rs = RandomizedSet()

    print(rs.insert(0))
    print(rs.insert(1))
    print(rs.insert(2))
    print(rs.insert(1))
    print(rs.remove(0))
    print(rs.getRandom())
