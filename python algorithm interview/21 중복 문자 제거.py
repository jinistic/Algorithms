from collections import deque, Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        https://leetcode.com/problems/remove-duplicate-letters/
        """
        # stack

        counter = Counter(s)
        stack = []

        for char in s:
            if char in stack:
                counter[char] -= 1
                continue

            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(char)
            counter[char] -= 1

        return "".join(stack)

        # recursion

        # if s == "":
        #     return ""

        # alphabets_set = set(s)
        # for char in sorted(alphabets_set):
        #     suffix = s[s.index(char) :]
        #     if set(suffix) == alphabets_set:
        #         return char + self.removeDuplicateLetters(suffix.replace(char, ""))


sol = Solution()
print(sol.removeDuplicateLetters("bcabc"))
print(sol.removeDuplicateLetters("abacb"))
print(sol.removeDuplicateLetters("cbacdcbc"))

