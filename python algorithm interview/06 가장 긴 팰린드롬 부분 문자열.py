from collections import defaultdict
from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 투 포인터가 중앙을 중심으로 확장하는 풀이 도전해 볼 것

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                str = s[start : start + length]
                if str == str[::-1]:
                    return str


sol = Solution()
print(sol.longestPalindrome(s="babad"))
