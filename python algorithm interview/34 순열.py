from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(map(list, itertools.permutations(nums)))

        answer = []
        path = []

        def dfs(numbers):
            if len(numbers) == 0:
                answer.append(path[:])
            for number in numbers:
                path.append(number)
                dfs(list(set(numbers) - set([number])))
                path.pop()

        dfs(nums)
        return answer


sol = Solution()
print(sol.permute([1, 2, 3]))
