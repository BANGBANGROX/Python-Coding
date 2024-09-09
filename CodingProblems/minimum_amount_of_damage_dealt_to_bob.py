from functools import cmp_to_key


class Solution:
    def minDamage(self, power: int, damage: list[int], health: list[int]) -> int:
        n: int = len(damage)
        times: list[int] = [0] * n
        indices: list[int] = [0] * n
        answer: int = 0
        current_time: int = 0

        for i in range(n):
            times[i] = (health[i] + power - 1) // power
            indices[i] = i

        indices.sort(
            key=cmp_to_key(lambda a, b: damage[b] * times[a] - damage[a] * times[b])
        )

        for idx in indices:
            current_time += times[idx]
            answer += current_time * damage[idx]

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        power: int = int(input())
        n: int = int(input())
        damage: list[int] = [0] * n
        for i in range(n):
            damage[i] = int(input())
        health: list[int] = [0] * n
        for i in range(n):
            health[i] = int(input())

        print(Solution().minDamage(power=power, damage=damage, health=health))
