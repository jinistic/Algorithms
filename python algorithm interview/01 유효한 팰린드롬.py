class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = []
        for s_ in s:
            if s_.isalnum():
                word.append(s_.lower())

        len_word = len(word)
        for i in range(len_word // 2):
            if word[i] != word[len_word - 1 - i]:
                return False

        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome("0p"))
