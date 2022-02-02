from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                day, _ = stack.pop()
                result[day] = i - day
            stack.append((i, t))
        return result


sol = Solution()
print(sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(sol.dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(sol.dailyTemperatures(temperatures=[30, 60, 90]))
