from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_to_letters_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        answer = []

        def dfs(index, path):
            print(index, path)
            if len(path) == len(digits):
                answer.append(path)
                return
            for i in range(index, len(digits)):
                for j in num_to_letters_dict[digits[i]]:
                    dfs(i + 1, path + j)

        dfs(0, "")
        return answer


sol = Solution()
print(sol.letterCombinations("23"))
